<template>
  <v-container style="margin-top: 12px; margin-bottom: 12px">
    <!--Head (Carousel) when screen is md and up-->
    <v-row v-show="$vuetify.breakpoint.mdAndUp">
      <v-col cols="12" sm="12" md="8">
        <v-card>
          <!--use object-fit: cover with 100% height to make horizontal overlapping possible-->
          <!--v-card style="height: 100%; object-fit: cover">
            <v-img src="@/assets/Home/img1.webp" style="height: 100%"></v-img>
          </v-card-->
          <v-carousel
            cycle
            hide-delimiter-background
            show-arrows-on-hover
          >
            <v-carousel-item
              v-for="(item,i) in items"
              :key="i"
              @click="navigateToLink(item.link)"
            >
              <v-img :src="require(`@/assets/Home/Carousel/${item.src}`)"></v-img>
            </v-carousel-item>
          </v-carousel>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="4">
        <!--v-card class="mx-auto" min-width="300" max-width="800" max-height="521" style="display: flex; flex-direction: column; justify-content: space-around; align-items: center;"-->
        <v-card style="height: 100%; display: flex; flex-direction: column; justify-content: space-around; align-items: center;">
          <v-card-text class="text-h5 text-center" style="padding-top: 45px; padding-bottom: 20px;">
            WELCOME
          </v-card-text>
          <v-card-text class="text-h4 text-center font-weight-bold" style="padding-top: -20px; padding-left: 30px; padding-right: 30px; padding-bottom: 40px; display: flex; flex-direction: column; align-items: center;">
            GIVING BACK TO OUR COMMUNITY THROUGH LIFE-CHANGING SERVICES.
          </v-card-text>
          <div style="padding-bottom: 50px; display: flex; flex-direction: column; justify-content: space-between; align-items: center;">
            <v-btn style="margin-bottom: 20px" @click="navigateToDonate()">
              ⚡️BOOST US⚡️
            </v-btn>
            <v-btn style="margin-bottom: 5px" @click="navigateToAbout()">
              LEARN MORE
            </v-btn>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <!--Head (Carousel) when screen is sm and down-->
    <v-row v-show="$vuetify.breakpoint.smAndDown">
      <v-col cols="12" xs="12" sm="12">
        <v-card>
          <v-carousel
            style="height: 300px; width: 100%"
            cycle
            hide-delimiter-background
            show-arrows-on-hover
          >
            <v-carousel-item
              style="width: 100%"
              v-for="(item,i) in items"
              :key="i"
              @click="navigateToLink(item.link)"
            >
              <v-img :src="require(`@/assets/Home/Carousel/${item.src}`)"></v-img>
            </v-carousel-item>
          </v-carousel>
        </v-card>
      </v-col>
      <v-col cols="12" xs="12" sm="12">
        <!--v-card class="mx-auto" min-width="300" max-width="800" max-height="521" style="display: flex; flex-direction: column; justify-content: space-around; align-items: center;"-->
        <v-card style="height: 100%; display: flex; flex-direction: column; justify-content: space-around; align-items: center;">
          <v-card-text class="text-h5 text-center" style="padding-top: 45px; padding-bottom: 20px;">
            WELCOME
          </v-card-text>
          <v-card-text class="text-h4 text-center font-weight-bold" style="padding-top: -20px; padding-left: 30px; padding-right: 30px; padding-bottom: 40px; display: flex; flex-direction: column; align-items: center;">
            GIVING BACK TO OUR COMMUNITY THROUGH LIFE-CHANGING SERVICES.
          </v-card-text>
          <div style="padding-bottom: 50px; display: flex; flex-direction: column; justify-content: space-between; align-items: center;">
            <v-btn style="margin-bottom: 20px" @click="navigateToDonate()">
              ⚡️BOOST US⚡️
            </v-btn>
            <v-btn style="margin-bottom: 5px" @click="navigateToAbout()">
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
          <v-btn style="margin-bottom: 20px;" @click="navigateToEvents()">VOLUNTEER</v-btn>
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
          <v-btn style="margin-bottom: 20px;" @click="navigateToAbout()">ABOUT US</v-btn>
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
          <v-btn style="margin-bottom: 20px;" @click="navigateToSupport()">SUPPORT</v-btn>
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
          <div style="width: 320px; margin-bottom: 12px; display: flex; flex-direction: row; justify-content: space-between; align-items: center">
            <div>
              <v-img src="@/assets/Home/target.png" max-width="60"></v-img>
            </div>
            <div>
              <v-img src="@/assets/Home/hh.png" max-width="100"></v-img>
            </div>
            <div>
              <v-img src="@/assets/Home/publix.png" max-width="70"></v-img>
            </div>
            <div>
              <v-img src="@/assets/Home/sams.png" max-width="80"></v-img>
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
        buttonLink: 'https://www.paypal.com/webapps/shoppingcart?flowlogging_id=f418588899cbc&mfid=1686273977343_f418588899cbc#/checkout/openButton',
        items: [
          {
            src: 'img1.webp',
            link: '/about'
          },
          {
            src: 'img2.jpg',
            link: '/events'
          }
        ],
      }
    },
    methods: {
      navigateToAbout() {
        this.$router.push('/about')
      },
      navigateToDonate() {
        this.$router.push('/donate')
      },
      navigateToEvents() {
        this.$router.push('/events')
      },
      navigateToSupport() {
        this.$router.push('/support')
      },
      navigateToLink(link) {
        this.$router.push(link)
      }
    }
  }
</script>