<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card class="mx-auto" max-width="800">
          <v-img src="@/assets/Home/img1.webp" max-width="800">
          </v-img>
        </v-card>
      </v-col>
      <v-col>
        <v-card class="mx-auto" min-width="300" max-width="800" max-height="521" style="display: flex; flex-direction: column; justify-content: space-around; align-items: center;">
          <v-card-text class="text-h5" style="margin-top: 45px; margin-bottom: 20px; display: flex; flex-direction: column; align-items: center;">
            WELCOME
          </v-card-text>
          <v-card-text class="text-h4 font-weight-bold" style="margin-top: -20px; padding-left: 30px; padding-right: 30px; margin-bottom: 20px; display: flex; flex-direction: column; align-items: center;">
            GIVING BACK TO OUR COMMUNITY THROUGH LIFE-CHANGING SERVICES.
          </v-card-text>
          <div style="padding-bottom: 50px; display: flex; flex-direction: column; justify-content: space-between; align-items: center;">
            <v-btn style="margin-bottom: 20px">
              JOIN US
            </v-btn>
            <v-btn>
              LEARN MORE
            </v-btn>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
    
<script>
  export default {
    name: 'HomeView',
    // 这里是组件的JavaScript代码
  }
</script>