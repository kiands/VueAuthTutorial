<template>
  <div>
    <div
      style="height: 8vh; padding: 10px; display: flex; flex-direction: row; justify-content: center; align-items: center"
    >
      <!--Navigation Drawer trigger button only exists on mdAndDown-->
      <v-navigation-drawer
        v-model="drawer"
        absolute
        temporary
      >
        <v-list
          nav
          dense
          v-for="item in items"
          :key="item"
        >
          <v-list-item @click="routeTo(links[item])">
            <v-list-item-title>{{ item }}</v-list-item-title>
          </v-list-item>
        </v-list>
        <div style="display: flex; justify-content: center">
          <v-btn @click="dialog = true" v-if="!this.$store.state.auth.isLoggedIn">SIGN IN/UP</v-btn>
          <v-btn @click="dialog = true" v-if="this.$store.state.auth.isLoggedIn">MANAGE</v-btn>
        </div>
      </v-navigation-drawer>
      <!--This div element contains the banner text and icons-->
      <div style="width: 95vw; display: flex; flex-direction: column; justify-content: space-between; align-items: center">
        <!--This will only show up on small and down screens-->
        <!--div :class="$vuetify.breakpoint.smAndDown ? 'banner-smAndDown' : 'banner-normal'"-->
        <div v-if="$vuetify.breakpoint.smAndDown" style="width: 100%; display: flex; flex-direction: column;">
          <div style="width: 100%; display: flex; flex-direction: row; justify-content: center">
            <div>678-765-0482</div>
            <div>&</div>
            <div>678-926-3808</div>
          </div>
          <div style="display: flex; flex-direction: row; justify-content: space-between; align-items: center">
            <v-btn icon @click.stop="drawer = !drawer">
              <v-icon>mdi-menu</v-icon>
            </v-btn>
            <div v-show="$vuetify.breakpoint.smAndDown" style="padding-left: 15px; padding-right: 15px; border-style: solid; border-width: 1px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
              <div style="font-size: 20px; font-weight: bold;">Face Friends</div>
              <div style="font-size: 20px; font-weight: bold;"> Foundation</div>
            </div>
            <v-btn icon>
              <v-icon>mdi-cart</v-icon>
            </v-btn>
          </div>
        </div>
        <!--This will only show up on medium and up screens-->
        <div v-if="$vuetify.breakpoint.mdAndUp" style="width: 100%; display: flex; flex-direction: row; justify-content: space-between; align-items: center;">
          <div style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <div>678-765-0482</div>
            <div>&</div>
            <div>678-926-3808</div>
          </div>
          <h1>Face Friends Foundation</h1>
          <!-- 添加一个按钮来打开登录对话框 -->
          <div>
            <v-btn icon @click="dialog = true" v-show="$vuetify.breakpoint.mdAndUp">
              <v-icon icon>
                mdi-account
              </v-icon>
            </v-btn>
            <v-btn icon>
              <v-icon>mdi-cart</v-icon>
            </v-btn>
          </div>
        </div>
      </div>
      <!-- 登录对话框 -->
      <v-dialog v-model="dialog" max-width="500px">
        <v-card>
          <!-- 在这里添加你的登录组件 -->
          <AuthComponent />
        </v-card>
      </v-dialog>
    </div>
    <v-card color="basil">
      <!--Don't know why class of md-and-up does not work-->
      <!--Use `activaTab` to bind highlight tab after each refresh-->
      <v-tabs
        v-model="activeTab"
        v-show="$vuetify.breakpoint.mdAndUp"
        background-color="transparent"
        grow
      >
        <v-tab
          v-for="item in items"
          :key="item"
          @click="routeTo(links[item])"
        >
          {{ item }}
        </v-tab>
      </v-tabs>
    </v-card>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld';
import AuthComponent from '@/components/AuthComponent';

export default {
  name: 'BannerComponent',

  components: {
    HelloWorld,
    AuthComponent
  },

  data () {
    return {
      activeTab: 0,
      drawer: false,
      dialog: false,
      items: [
        'Home',
        'About Us',
        'Services',
        'Donate and Sponsor',
        'Ways to Support',
        'Events',
        'Contact Us',
        'More'
      ],
      links: {
        'Home': '/',
        'About Us': '/about',
        'Services': '/services',
        'Ways to Support': '/support',
        'Events': '/events',
        'Donate and Sponsor': '/donate',
        'Contact Us': '/contact'
        // 'More': '/more'
      }
    }
  },

  watch: {
    '$route': {
      immediate: true,
      handler(to, from) {
        // 在这里根据当前路由来设置 activeTab 的值
        // 例如，如果路由匹配 links 的某个元素，你可以找到它的索引并设置 activeTab
        const index = this.items.findIndex(item => this.links[item] === to.path);
        if (index >= 0) {
          this.activeTab = index;
        }
      }
    }
  },

  methods: {
    // Avoid a stupid error: NavigationDuplicated: Avoided redundant navigation to current location
    routeTo(route) {
      this.$router.push(route).catch(error => {
        if (error.name !== 'NavigationDuplicated') {
          // 如果不是 NavigationDuplicated 错误，抛出错误
          throw error;
        }
      });
    }
  }
};
</script>
