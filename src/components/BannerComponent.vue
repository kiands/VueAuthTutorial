<template>
  <div>
      <div
        style="
        height: 10vh;
        padding: 10px;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;"
      >
        <div>3473400000</div>
        <h1 class="font-weight-bold text-h3">
          FACE FRIENDS FOUNDATION
        </h1>
        <!-- 添加一个按钮来打开登录对话框 -->
        <v-btn color="white" @click="dialog = true">
          <v-icon>
            mdi-account
          </v-icon>
        </v-btn>
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
        <v-tabs
          v-show="$vuetify.breakpoint.mdAndUp"
          background-color="transparent"
          grow
        >
          <v-tab
            v-for="item in items"
            :key="item"
            @click="$router.push(item[1])"
          >
            {{ item[0] }}
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
      dialog: false,
      items: [
        ['Home', '/'],
        ['About Us', '/about'],
        ['Services', '/services'],
        ['Volunteer', '/volunteer'],
        ['Support', '/support'],
        ['Events', '/events'],
        ['Become a Sponsor', '/sponsor'],
        ['More', '/more']
      ]
    }
  },
};
</script>
