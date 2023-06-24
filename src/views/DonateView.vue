<template>
  <v-container style="margin-bottom: 12px">
    <v-row>
      <v-col style="display: flex; flex-direction: column; align-items: center">
        <v-card-text class="text-h4 text-center font-weight-bold" style="padding-top: -20px; padding-left: 30px; padding-right: 30px">
          WELCOME TO THE FACE FRIENDS FOUNDATION!
        </v-card-text>
        <v-card-text style="font-size: 24px; line-height: 30px; color: grey">
          We are a charitable organization dedicated to improving the lives of those in need. Join us in making a difference today! 100% of your donation will fund our mission to provide support and improve conditions for impoverished individuals and families. All donations are tax deductible.
        </v-card-text>
        <v-btn style="margin-top: 12px" @click="navigateToAbout()">
          FIND OUT MORE
        </v-btn>
      </v-col>
    </v-row>
    <v-row style="margin-top: 24px">
      <v-col style="display: flex; flex-direction: column; align-items: center; justify-content: center">
        <div style="font-size: 24px; margin-bottom: 12px">
          Donate Today
        </div>
        <v-card max-width="400px">
          <v-img src="@/assets/Donate/donorbox.png"></v-img>
        </v-card>
      </v-col>
    </v-row>
    <!--honors-->
    <v-row>
      <v-col xs="12" sm="6">
        <v-card style="height: 100%; object-fit: cover">
          <v-img src="@/assets/Donate/flag.webp" style="height: 100%"></v-img>
        </v-card>
      </v-col>
      <v-col xs="12" sm="6">
        <v-card style="height: 100%">
          <v-card-text class="text-h4 font-weight-bold" style="margin-bottom: 4px">
            TIER1 SPONSORSHIP
          </v-card-text>
          <v-card-text style="font-size: 24px;">
            $500
          </v-card-text>
          <div style="margin-top: 20px; margin-left: 20px; margin-bottom: 20px">
            <div style="display: flex; flex-direction: column; justify-content: center;">
              <div>
                <v-btn style="margin-bottom: 20px;" :href="buttonLink" target="_blank">Donate</v-btn>
              </div>
              <v-img src="@/assets/Donate/payments.png" max-width="240"></v-img>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col xs="12" sm="6">
        <v-card style="height: 100%; object-fit: cover">
          <v-img src="@/assets/Donate/flag.webp" style="height: 100%"></v-img>
        </v-card>
      </v-col>
      <v-col xs="12" sm="6">
        <v-card style="height: 100%">
          <v-card-text class="text-h4 font-weight-bold" style="margin-bottom: 4px">
            TIER2 SPONSORSHIP
          </v-card-text>
          <v-card-text style="font-size: 24px;">
            $1000
          </v-card-text>
          <div style="margin-top: 20px; margin-left: 20px; margin-bottom: 20px">
            <div style="display: flex; flex-direction: column; justify-content: center;">
              <div>
                <v-btn style="margin-bottom: 20px;" :href="buttonLink" target="_blank">Donate</v-btn>
              </div>
              <v-img src="@/assets/Donate/payments.png" max-width="240"></v-img>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'SponsorView',
    // 这里是组件的JavaScript代码
    methods: {
      navigateToAbout() {
        this.$router.push('/about')
      }
    }
  }
</script>

<style scoped>
  /* 这里是关于页面的CSS样式 */
</style>  