<template>
  <div>
      <div
        style="
        height: 10vh;
        padding: 10px;
        display: flex;
        flex-direction: row;
        justify-content: center;"
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
          >
            <v-list-item-group
              v-model="group"
              active-class="deep-purple--text text--accent-4"
            >
              <v-list-item>
                <v-list-item-title>Foo</v-list-item-title>
              </v-list-item>

              <v-list-item>
                <v-list-item-title>Bar</v-list-item-title>
              </v-list-item>

              <v-list-item>
                <v-list-item-title>Fizz</v-list-item-title>
              </v-list-item>

              <v-list-item>
                <v-list-item-title>Buzz</v-list-item-title>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-navigation-drawer>
        <div style="width: 95vw; display: flex; flex-direction: column; justify-content: space-between; align-items: center">
          <!--This will only show up on small and down screens-->
          <div v-show="$vuetify.breakpoint.smAndDown">3473400000</div>
          <div :class="$vuetify.breakpoint.smAndDown ? 'banner-smAndDown' : 'banner-normal'">
            <div v-show="$vuetify.breakpoint.mdAndUp" style="display: flex; align-items: center">3473400000</div>
            <v-btn icon @click.stop="drawer = !drawer" v-show="$vuetify.breakpoint.smAndDown">
              <v-icon>mdi-magnify</v-icon>
            </v-btn>
            <h1 :class="$vuetify.breakpoint.smAndDown ? 'small-text' : 'normal-text'">FACE FRIENDS FOUNDATION</h1>
            <!-- 添加一个按钮来打开登录对话框 -->
            <v-btn icon @click="dialog = true" v-show="$vuetify.breakpoint.mdAndUp">
              <v-icon icon>
                mdi-account
              </v-icon>
            </v-btn>
            <div v-show="$vuetify.breakpoint.smAndDown"></div>
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

<style>
.banner-normal {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center
}

.banner-smAndDown {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center
}

.small-text {
  font-size: 1.5rem;
  display: flex;
  align-items: center
}

.normal-text {
  font-size: 3rem;
}
</style>

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
      drawer: false,
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
