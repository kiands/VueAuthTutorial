<template>
  <v-app>
  <div id="app" style="display: flex; flex-direction: column; justify-content: flex-start;">
    <div>
      <BannerComponent/>
    </div>
    <!--div>
      <router-link to="/login">login</router-link>
    </div-->
    <router-view />
  </div>
  <v-footer
    padless
  >

    <v-card
      flat
      tile
      class="lighten-1 text-center"
    >
      <v-divider></v-divider>
      <v-card-text>
        <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-4"
          icon
        >
          <v-icon size="24px">
            {{ icon }}
          </v-icon>
        </v-btn>
      </v-card-text>

      <v-card-text class="pt-0" style="width: 100vw">
        If you need help or want to contact us for events and volunteering, please dial 678-765-0482 or 678-926-3808 :)
      </v-card-text>

      <v-card-text>
        © {{ new Date().getFullYear() }} — <strong>Face Friends Foundation</strong>
      </v-card-text>
    </v-card>
  </v-footer>
  </v-app>
</template>

<script>
import BannerComponent from '@/components/BannerComponent';

export default {
  components: { BannerComponent },
  name: 'App',
  data() {
    return {
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ]
    }
  }
};

</script>
