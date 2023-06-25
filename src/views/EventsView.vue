<template>
  <v-container style="margin-top: 12px; margin-bottom: 12px">
    <v-row>
      <v-col>
        <strong>CURRENT EVENTS</strong>
      </v-col>
    </v-row>
    <!--Line1-->
    <v-row cols="12" :class="$vuetify.breakpoint.smAndDown ? 'vrow-smAndDown' : 'vrow-normal'">
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card>
          <v-img src="@/assets/Events/e1.webp"></v-img>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <div style="height: 100%">
          <div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="text--title">Get Involved</div>
            <div class="text--body">We're always looking for volunteers and fundraisers to help us provide services to the community. Please let us know how you'd like to help.</div>
            <v-btn style="margin-top: 8px" @click="navigateToContact()">CONTACT US</v-btn>
          </div>
        </div>
      </v-col>
    </v-row>
    <!--Line2-->
    <v-row cols="12">
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <div style="height: 100%">
          <div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="text--title">Summer Backpack and School Supply Drive</div>
            <div class="text--body">We're in full gear to raise funds and in-kind donations for our Summer Backpack and School Supply Drive. Any help is much appreciated!</div>
            <v-btn style="margin-top: 8px" :href="link1" target="_blank">LEARN MORE</v-btn>
          </div>
        </div>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card>
          <v-img src="@/assets/Events/e2.webp"></v-img>
        </v-card>
      </v-col>
    </v-row>
    <!--Line3-->
    <v-row cols="12" :class="$vuetify.breakpoint.smAndDown ? 'vrow-smAndDown' : 'vrow-normal'">
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card>
          <v-img src="@/assets/Events/e3.webp"></v-img>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <div style="height: 100%">
          <div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="text--title">Krispy Kreme Fundraiser</div>
            <div class="text--body">
              <div>We're raising funds with Digital Dozens-it's a great way to support our causes virtually!</div>
              <div>Digital Dozen Certificates are valid for One Dozen Original Glazed Doughnuts and will be emailed to you after purchase. The certificates can be redeemed at any Krispy Kreme location. The cost is $14/dozen.</div>
              <div>Together we can make a difference for those in need in our community.</div>
            </div>
            <v-btn style="margin-top: 8px" :href="link2" target="_blank">PURCHASE A CERTIFICATE</v-btn>
          </div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'EventsView',
    // 这里是组件的JavaScript代码
    data() {
      return {
        link1: "https://app.kambeo.io/event/help.us.raise.funds.for.atr",
        link2: "https://app.kambeo.io/event/krispykremefundraiser"
      }
    },
    methods: {
      navigateToContact() {
        this.$router.push('/contact')
      }
    }
  }
</script>

<style scoped>
  /* 这里是关于页面的CSS样式 */
  .vrow-smAndDown {
    display: flex;
    flex-direction: column-reverse
  }
  .vrow-normal {
    display: flex;
    flex-direction: row
  }
  .text--title {
    text-align: center;
    font-size: 24px
  }

  .text--body {
    text-align: center;
    color: gray
  }
</style>