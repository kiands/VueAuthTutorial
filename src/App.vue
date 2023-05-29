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
  </v-app>
</template>

<script>
import BannerComponent from '@/components/BannerComponent';

export default {
  components: { BannerComponent },
  name: 'App',
};

</script>
