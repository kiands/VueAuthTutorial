<template>
  <v-container>
    <!--Head-->
    <v-row>
      <v-col cols="12" sm="12" md="8">
        <!--v-card class="mx-auto" max-width="800"-->
        <v-card style="height: 100%; object-fit: cover">
          <v-img src="@/assets/Home/img1.webp" style="height: 100%"></v-img>
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
    <!--Team History Mission-->
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
    <!--Donation-->
    <v-row>
      <v-col cols="12" xs="12" sm="6">
        <v-card style="height: 100%; object-fit: cover">
          <v-img src="@/assets/Home/img2.webp" style="height: 100%"></v-img>
        </v-card>
      </v-col>
      <v-col cols="12" xs="12" sm="6">
        <v-card style="height: 100%">
          <v-card-text class="text-h4 font-weight-bold" style="margin-bottom: 4px">
            HELP OUR CAUSE
          </v-card-text>
          <div style="margin-left: 20px; margin-bottom: 20px">
            <div style="display: flex; flex-direction: column; justify-content: center;">
              <div>
                <v-btn style="margin-bottom: 20px;" :href="buttonLink" target="_blank">Donate</v-btn>
              </div>
              <v-img src="@/assets/Home/payments.png" max-width="200"></v-img>
            </div>
          </div>
          <v-card-text>
            100% of your donation will fund our mission to provide support and improve conditions for those in need. All donations are tax deductible.
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <!--Fundraising flyer-->
    <v-row>
      <v-col>
        <v-card col="12" xs="12" sm="12" md="12" lg="12" xl="12" style="display: flex; flex-direction: column; justify-content: center; align-items: center">
          <v-img src="@/assets/Home/fundraising.webp"></v-img>
          <v-btn style="margin-bottom: 24px">BUY A DOZEN TODAY</v-btn>
        </v-card>
      </v-col>
    </v-row>
    <!--Sponsors-->
    <v-row>
      <v-col>
        <v-card style="display: flex; flex-direction: column; align-items: center">
          <v-card-text class="text-h4 font-weight-bold" style="display: flex; flex-direction: column; align-items: center">
            OUR SPONSORS
          </v-card-text>
          <div style="width: 500px; margin-bottom: 12px; display: flex; flex-direction: row; justify-content: space-between; align-items: center">
            <div>
              <v-img src="@/assets/Home/target.webp" max-width="50"></v-img>
            </div>
            <div>
              <v-img src="@/assets/Home/hh.webp" max-width="100"></v-img>
            </div>
            <div>
              <v-img src="@/assets/Home/publix.webp" max-width="100"></v-img>
            </div>
            <div>
              <v-img src="@/assets/Home/sams.webp" max-width="100"></v-img>
            </div>
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
    data() {
      return {
        buttonLink: 'https://www.paypal.com/webapps/shoppingcart?flowlogging_id=f418588899cbc&mfid=1686273977343_f418588899cbc#/checkout/openButton'
      }
    }
  }
</script>