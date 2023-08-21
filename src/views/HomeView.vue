<template>
  <v-container style="margin-bottom: 12px;">
    <!--Head (Carousel) when screen is md and up-->
    <v-row v-show="$vuetify.breakpoint.mdAndUp">
      <v-col cols="12" sm="12" md="8" style="display: flex; flex-grow: 1">
        <v-card style="width: 100%; object-fit: cover">
          <!--use object-fit: cover with 100% height to make horizontal overlapping possible-->
          <!--v-card style="height: 100%; object-fit: cover">
            <v-img src="@/assets/Home/img1.webp" style="height: 100%"></v-img>
          </v-card-->
          <v-carousel
            cycle
            hide-delimiters
          >
            <v-carousel-item
              v-for="(item,i) in carousels"
              :key="i"
              @click="navigateToLink(item.link)"
              :src="item.source"
            >
            </v-carousel-item>
          </v-carousel>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="4">
        <!--v-card class="mx-auto" min-width="300" max-width="800" max-height="521" style="display: flex; flex-direction: column; justify-content: space-around; align-items: center;"-->
        <v-card style="height: 100%; display: flex; flex-direction: column; justify-content: space-evenly; align-items: center;">
          <v-card-text class="text-h5 text-center" style="padding-top: 25px;">
            WELCOME!
          </v-card-text>
          <v-card-text class="text-h4 text-center font-weight-bold" style="padding-top: -20px; padding-left: 30px; padding-right: 30px; padding-bottom: 30px; display: flex; flex-direction: column; align-items: center;">
            GIVING BACK TO OUR COMMUNITY THROUGH LIFE-CHANGING SERVICES.
          </v-card-text>
          <div style="padding-bottom: 35px; padding-left: 0; display: flex; flex-direction: row; justify-content: space-between; align-items: center;">
            <v-btn style="margin-right:15px" @click="navigateToDonate()">
              DONATE
            </v-btn>
            <v-btn @click="navigateToAbout()">
              LEARN MORE
            </v-btn>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <!--Head (Carousel) when screen is sm and down-->
    <v-row v-show="$vuetify.breakpoint.smAndDown">
      <v-col cols="12" xs="12" sm="12">
        <!--v-card style="display: flex; flex-direction: row; justify-content: center; align-items: center; height: 400px"-->
          <!--v-carousel
            cycle
            hide-delimiter-background
            show-arrows-on-hover
          >
            <v-carousel-item
              v-for="(item,i) in carousels"
              :key="i"
              @click="navigateToLink(item.link)"
            >
              <v-img :src=item.source style="height: 400px; width: auto; object-fit: contain;"/>
            </v-carousel-item>
          </v-carousel-->
          <!--The native v-carousel is ugly and weired, I decide to use JS implementation-->
        <!--/v-card-->
        <v-carousel
            cycle
            hide-delimiter-background
            show-arrows-on-hover
            style="height: 400px"
          >
            <v-carousel-item
              v-for="(item,i) in carousels"
              :key="i"
              @click="navigateToLink(item.link)"
            >
                <v-img :src=item.source style="height: 80%; width: auto; object-fit: cover;" />
            </v-carousel-item>
          </v-carousel>
      </v-col>
      <v-col cols="12" xs="12" sm="12">
        <!--v-card class="mx-auto" min-width="300" max-width="800" max-height="521" style="display: flex; flex-direction: column; justify-content: space-around; align-items: center;"-->
        <div style="height: 100%; display: flex; flex-direction: column; justify-content: space-around; align-items: center;">
          <v-card-text class="text-h5 text-center" style="padding-top: 10px; padding-bottom: 20px;">
            WELCOME!
          </v-card-text>
          <v-card-text class="text-h4 text-center font-weight-bold" style="padding-top: -20px; padding-left: 30px; padding-right: 30px; padding-bottom: 30px; display: flex; flex-direction: column; align-items: center;">
            GIVING BACK TO OUR COMMUNITY THROUGH LIFE-CHANGING SERVICES.
          </v-card-text>
          <div style="padding-bottom: 35px; padding-left: 0; display: flex; flex-direction: row; justify-content: space-between; align-items: center;">
            <v-btn style="margin-right:15px" @click="navigateToDonate()">
              DONATE
            </v-btn>
            <v-btn @click="navigateToAbout()">
              LEARN MORE
            </v-btn>
          </div>
        </div>
      </v-col>
    </v-row>
    <!--Team History Mission-->
    <!--Vuetify grid: those break points' work mode is `andUp`. Each screen size is divided in 12 cols-->
    <v-row style="display: flex; flex-direction: row; justify-content: center">
      <v-col cols="12" xs="12" sm="6" md="4">
        <v-card style="height: 100%; display: flex; flex-direction: column; align-items: center;">
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
        <v-card style="height: 100%; display: flex; flex-direction: column; align-items: center;">
          <v-img src="@/assets/Home/fx-gs-1.webp" max-width="270"></v-img>
          <v-card-text class="text-h4 text-center">
            OUR HISTORY
          </v-card-text>
          <v-card-text>
            Seeing a need for energetic, nonprofit work in this area, we formed the Face Friends Foundation to provide sensible solutions. We've consistently grown since then, all thanks to the helping hands of this amazing community!
          </v-card-text>
          <v-btn style="margin-bottom: 20px;" @click="navigateToAbout()">ABOUT US</v-btn>
        </v-card>
      </v-col>
      <v-col cols="12" xs="12" sm="6" md="4">
        <v-card style="height: 100%; display: flex; flex-direction: column; align-items: center;">
          <v-img src="@/assets/Home/fx-gs-2.webp" max-width="270"></v-img>
          <v-card-text class="text-h4 text-center">
            OUR MISSION
          </v-card-text>
          <v-card-text>
            We focus on making the maximum positive impact on our community. Our members and volunteers provide the momentum that helps us affect change. Using data driven models, we provide solutions that make a long-lasting difference.
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
          <div>
            <!-- xs size -->
            <v-row v-if="$vuetify.breakpoint.xsOnly" class="justify-center">
              <v-col v-for="(sponsor, index) in sponsors" :key="index" cols="4" class="d-flex align-center justify-center">
                <img :src="sponsor.source" alt="Sponsor" class="sponsor-image">
              </v-col>
            </v-row>

            <!-- sm size -->
            <v-row v-else-if="$vuetify.breakpoint.smOnly" class="justify-center">
              <v-col v-for="(sponsor, index) in sponsors" :key="index" cols="3" class="d-flex align-center justify-center">
                <img :src="sponsor.source" alt="Sponsor" class="sponsor-image">
              </v-col>
            </v-row>

            <!-- mdAndUp size -->
            <v-row v-else class="justify-center">
              <v-col v-for="(sponsor, index) in sponsors" :key="index" cols="2" class="d-flex align-center justify-center">
                <img :src="sponsor.source" alt="Sponsor" class="sponsor-image">
              </v-col>
            </v-row>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.sponsor-image {
  width: 100%;
  height: auto;
}
</style>

<script>
  import apiClient from "@/api.js"
  export default {
    name: 'HomeView',
    mounted() {
      this.initialize()
    },
    data() {
      return {
        carousels: [],
        sponsors: [],
        buttonLink: 'https://www.paypal.com/webapps/shoppingcart?flowlogging_id=f418588899cbc&mfid=1686273977343_f418588899cbc#/checkout/openButton',
      }
    },
    methods: {
      initialize() {
        apiClient.get("cms/carousels").then(response => {
          this.carousels = response.data.carousels
        })
        apiClient.get("cms/sponsors").then(response => {
          this.sponsors = response.data.sponsors
        })
      },
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