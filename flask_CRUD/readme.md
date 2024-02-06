有关服务预订取消系统中Redis的使用

首先说一下services表结构以及范例数据：

| service\_id | service\_name | service\_description | time\_slots |
| --- | --- | --- | --- |
| 1 | Utility Bill Assistance | Maximum assistance is US $100 per client in a twelve month period. You must bring with you a current utility bill. | {"2023-06-13": {"07:00": 25, "09:00": 29}, "2023-06-14": {"08:00": 6, "10:00": 4}} |

按理说这个违反1NF的设计可以用nosql来解决，但是因为大部分的网站数据都是关系型的，所以这边就偷懒用了MySQL，毕竟MySQL后来也支持了JSON数据类型，而不是单纯往这个字段里加JSON形态的"集合文字"。

其次说一下用户预订行为发生后对time\_slots的更新逻辑：

这个time\_slots的键值对结构是 { date: { time: remaining } }。在系统中用户只能预订一个服务，由对应的API和booked\_services表控制，这段不展开。总之已经注册且登陆的用户在前端由date，time定位到具体的服务时，可以根据remaining是否允许预订进行相应的操作。

用户完成预订之后就要对这个time\_slots的相应键值对进行修改。这里就引出了Flask的线程安全性和后端编程中部分需要共享且进行多对一抢占式修改、一对多读取的数据的线程安全性问题。

已知Flask的每个API中，每个请求的所关联的方法成员变量可以交给Flask去管理，不存在什么问题。但是这个time\_slots其实是一个需要共享的变量：查询某天某时间段的剩余变量要看它，订阅要修改它，取消也要修改它。这就导致会发生请求量高时多个请求的业务逻辑可能会同时读取/写入。这样就需要加锁了。在Python中，大概就是这么个情况：
```
# 导入的其它相关包
import threading # 与"线程"，锁相关
# Flask业务模块蓝图初始化时的其它代码
lock = threading.Lock() # 创建锁实例
global_json_data = {} # 初始化共享变量

@app.route('/update', methods=['POST']) # 范例API
def update\_data():
    global global_json_data
    data = request.get\_json()

    with lock:
        # 安全地修改全局变量
        global_json_data.update(data)
        # 可以选择在这里同步更新Redis
        redis_client.set("global_json_key", json.dumps(global_json_data))

    return jsonify(success=True)
```

这里不太会出现死锁的情况，因为不满足死锁产生的条件。是很单纯的先到先得，修改完就释放。

然后就是关于Redis的参与。其实这个情况下Redis参与不参与问题不大。JSON作为全局变量出现在内存中本身也很快了。不过考虑到以下业务逻辑的实现，用Redis其实也不是不可以：

模仿一些银行的业务，每天到凌晨某时候暂停业务，对数据进行持久化。Flask框架中做这个类似定时任务的实现比较冷门，所以如果有Redis的话，可以绕开Python和这个框架在操作系统中执行Redis和MySQL的同步。

| 上一次同步任务完成 |
| --- |
| 服务启动 |
| 读取数据库time\_slots，保存为API之外的json变量 |
| 同步这个json变量到Redis |
| 执行前文所述加锁的业务逻辑 |
| 到预订的维护时间，暂停一切外来的请求并执行Redis和同步数据库的同步 |

注意：上表排列的任务需要严格串行化执行

相对于上面这个逻辑用Redis稍显牵强，下面还有一个对线程安全性要求低但是又更加简单的业务对缓存是刚需。

先看表

| booking\_id | user\_id | service\_name | date | time | status | message |
| --- | --- | --- | --- | --- | --- | --- |
| 31 | 2 | Food Assistance | 2023-06-12 | 08:00 | 0 | NULL |

最传统的前后端分离网站自然是用户刷新一次，就触发本页面上所有预设的请求。对于本项目的服务页面，已经登陆的用户刷新页面会自动触发"查询已经预定的服务"的功能。显然这对于直连数据库很不友好。这时候如果能把相应的数据存入Redis，就会很方便。这依然只用到基础的Redis键值对。

本项目的设计从源头控制了能查询到的已预订服务数量（仅为1），也就是status = 0的"已申请未批准"。所以在Redis中的键值对，键是user\_id，值是为业务逻辑进行了对应格式封装的booking\_id，service\_name，date，time，status和message。应用类似的每日定时持久化逻辑，在接受业务的时段我们可以仅凭借Redis缓存达到更好的响应而且可以不在业务时段进行数据库同步。

需要注意的是，在前端限制频繁刷新或者研究其它的缓存方式仍然是必要的。