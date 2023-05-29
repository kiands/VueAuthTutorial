<template>
  <div>
    <div class="container">
      <img src="@/assets/Home/img1.webp" alt="img1" />
      <div style="display: flex; flex-direction: column; justify-content: space-around; align-items: center;">
        <div>WELCOME</div>
        <h1>GIVING BACK TO OUR COMMUNITY THROUGH LIFE-CHANGING SERVICES.</h1>
        <div style="display: flex; flex-direction: column; justify-content: space-around; align-items: center;">
          <v-btn>JOIN US</v-btn>
          <v-btn>LEARN MORE</v-btn>
        </div>
      </div>
    </div>
  </div>
</template>
    
<script>
  export default {
    name: 'HomeView',
    // 这里是组件的JavaScript代码
  }
</script>
  
<style>
  .container {
    width: 80vw; /* 上一层 div 的宽度 */
    overflow: hidden; /* 隐藏超出部分 */
    display: flex;
    flex-direction: row;
  }
  .container img {
    max-width: 70%;
    max-height: 70%;
    display: block; /* 图片以块级元素显示，避免与其他内容混排 */
  }
</style>