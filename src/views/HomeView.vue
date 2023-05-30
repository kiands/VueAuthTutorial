<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="12" md="8">
        <!--v-card class="mx-auto" max-width="800"-->
        <v-card>
          <v-img src="@/assets/Home/img1.webp">
          </v-img>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="4" style="height: auto">
        <!--v-card class="mx-auto" min-width="300" max-width="800" max-height="521" style="display: flex; flex-direction: column; justify-content: space-around; align-items: center;"-->
        <v-card style="display: flex; flex-direction: column; justify-content: space-around; align-items: center;">
          <v-card-text class="text-h5 text-center" style="padding-top: 45px; padding-bottom: 20px;">
            WELCOME
          </v-card-text>
          <v-card-text class="text-h4 text-center font-weight-bold" style="padding-top: -20px; padding-left: 30px; padding-right: 30px; padding-bottom: 40px; display: flex; flex-direction: column; align-items: center;">
            GIVING BACK TO OUR COMMUNITY THROUGH LIFE-CHANGING SERVICES.
          </v-card-text>
          <div style="padding-bottom: 50px; display: flex; flex-direction: column; justify-content: space-between; align-items: center;">
            <v-btn style="margin-bottom: 20px">
              JOIN US
            </v-btn>
            <v-btn style="margin-bottom: 5px">
              LEARN MORE
            </v-btn>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <!--Vuetify grid: those break points' work mode is `andUp`. Each screen size is divided in 12 cols-->
    <v-row style="display: flex; flex-direction: row; justify-content: center">
      <v-col cols="12" xs="12" sm="6" md="4">
        <v-card style="display: flex; flex-direction: column; align-items: center;">
          <v-img src="@/assets/Home/fx-gs.webp" max-width="270"></v-img>
          <v-card-text class="text-h4 text-center">
            OUR TEAM
          </v-card-text>
          <v-card-text>
            Our amazing team of regular and part-time volunteers are committed to helping others. We take our convictions and turn them into action. Do you think you would be a good fit? Please get in touch for more information!
          </v-card-text>
          <v-btn style="margin-bottom: 20px;"></v-btn>
        </v-card>
      </v-col>
      <v-col cols="12" xs="12" sm="6" md="4">
        <v-card style="display: flex; flex-direction: column; align-items: center;">
          <v-img src="@/assets/Home/fx-gs-1.webp" max-width="270"></v-img>
          <v-card-text class="text-h4 text-center">
            OUR HISTORY
          </v-card-text>
          <v-card-text>
            Our amazing team of regular and part-time volunteers are committed to helping others. We take our convictions and turn them into action. Do you think you would be a good fit? Please get in touch for more information!
          </v-card-text>
          <v-btn style="margin-bottom: 20px;"></v-btn>
        </v-card>
      </v-col>
      <v-col cols="12" xs="12" sm="6" md="4">
        <v-card style="display: flex; flex-direction: column; align-items: center;">
          <v-img src="@/assets/Home/fx-gs-2.webp" max-width="270"></v-img>
          <v-card-text class="text-h4 text-center">
            OUR MISSION
          </v-card-text>
          <v-card-text>
            Our amazing team of regular and part-time volunteers are committed to helping others. We take our convictions and turn them into action. Do you think you would be a good fit? Please get in touch for more information!
          </v-card-text>
          <v-btn style="margin-bottom: 20px;"></v-btn>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" xs="12" sm="6">
        <v-card>
          <v-img src="@/assets/Home/img2.webp" max-width="600"></v-img>
        </v-card>
      </v-col>
      <v-col cols="12" xs="12" sm="6">
        <v-card>
          <v-card-text class="text-h4 font-weight-bold">
            HELP OUR CAUSE
          </v-card-text>
          <v-card-text class="text-h4 font-weight-bold">
            PayPal Placeholder
          </v-card-text>
          <div style="display: flex; justify-content: center;">
            <v-btn style="margin-bottom: 20px;"></v-btn>
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