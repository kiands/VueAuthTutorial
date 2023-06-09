<template>
  <v-container style="margin-top: 12px; margin-bottom: 12px">
    <v-row>
      <v-col>
        <strong>OUR PROGRAMS</strong>
      </v-col>
    </v-row>
    <!--Line1-->
    <v-row cols="12" :class="$vuetify.breakpoint.smAndDown ? 'vrow-smAndDown' : 'vrow-normal'">
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card>
          <v-img src="@/assets/About/backpack.webp"></v-img>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <div style="height: 100%">
          <div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="text--title">Summer Backpack and School Supply Giveaway</div>
            <div class="text--body">Face Friends Foundation sponsored the Easter Bun and Cheese program and we served over thirty families with Easter Bun and Cheese, well done team</div>
          </div>
        </div>
      </v-col>
    </v-row>
    <!--Line2-->
    <v-row cols="12">
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <div style="height: 100%">
          <div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="text--title">Easter Bun and Cheese Program</div>
            <div class="text--body">Face Friends Foundation provides free backpacks and school supplies to children in need</div>
          </div>
        </div>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card>
          <v-img src="@/assets/About/bun.webp"></v-img>
        </v-card>
      </v-col>
    </v-row>
    <!--Line3-->
    <v-row cols="12" :class="$vuetify.breakpoint.smAndDown ? 'vrow-smAndDown' : 'vrow-normal'">
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card>
          <v-img src="@/assets/About/gift.webp"></v-img>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <div style="height: 100%">
          <div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="text--title">Target Store Sponsors of Great Giftogether</div>
            <div class="text--body">Face Friends Foundation was selected by Target Stores in Suwannee Georgia to be a recipient of the Great Giftogether Program, we selected two needy families from our pool of clients and Target 🎯 in turn donated holiday gifts 🎁 and necessities for these families. We salute Target stores for their great work in the community.</div>
          </div>
        </div>
      </v-col>
    </v-row>
    <!--Line4-->
    <v-row cols="12">
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <div style="height: 100%">
          <div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="text--title">Food and Clothing Assistance</div>
            <div class="text--body">Face Friends Foundation provides food and clothing assistance</div>
          </div>
        </div>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card>
          <v-img src="@/assets/About/food.webp"></v-img>
        </v-card>
      </v-col>
    </v-row>
    <!--Line5-->
    <v-row cols="12" :class="$vuetify.breakpoint.smAndDown ? 'vrow-smAndDown' : 'vrow-normal'">
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card>
          <v-img src="@/assets/About/emergency.webp"></v-img>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <div style="height: 100%">
          <div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="text--title">Utility and Emergency Services Assistance</div>
            <div class="text--body">Face Friends Foundation provides help with utility bills and emergency funds</div>
          </div>
        </div>
      </v-col>
    </v-row>
    <!--Line6-->
    <v-row cols="12">
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <div style="height: 100%">
          <div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="text--title">Free Online Tutoring</div>
            <div class="text--body">Face Friends Foundation provides free online tutoring services for grades K-12</div>
          </div>
        </div>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card>
          <v-img src="@/assets/About/tutor.webp"></v-img>
        </v-card>
      </v-col>
    </v-row>
    <!--Board-->
    <v-row style="margin-top:24px; margin-bottom: 24px">
      <v-col>
        <div>BOARD OF DIRECTORS AND STAFF</div>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card style="height: 100%">
          <v-card-title>Board President</v-card-title>
          <v-img src="@/assets/About/Winston.webp" />
          <v-card-text>Winston G. Guy is the Founder, President and Executive Director of Face Friends Foundation.</v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card style="height: 100%">
          <v-card-title>Board Vice President</v-card-title>
          <v-img src="@/assets/About/Jean.webp" />
          <v-card-text>Jean Raymond id the Vice President of Face Friends Foundation.</v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card style="height: 100%">
          <v-card-title>Board Treasurer</v-card-title>
          <v-img src="@/assets/About/Ann-Marie.webp" />
          <v-card-text>Ann-Marie Brown is the Treasurer of Face Friends Foundation.</v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card style="height: 100%">
          <v-card-title>Board Secretary</v-card-title>
          <v-img src="@/assets/About/Veronica.webp" />
          <v-card-text>Veronica Wilson is the Secretary of Face Friends Foundation.</v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <!--Memboers of the board-->
    <v-row style="margin-top:24px; margin-bottom: 24px">
      <v-col>
        <div>MEMBERS OF THE BOARD</div>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card style="height: 100%">
          <v-card-title>Member of the Board</v-card-title>
          <v-img src="@/assets/About/Leroy.webp" />
          <v-card-text>Leroy Mair is a member of Face Friends Foundation Board of Directors.</v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card style="height: 100%">
          <v-card-title>Member of the Board</v-card-title>
          <v-img src="@/assets/About/Betty.webp" />
          <v-card-text>Betty DeRamus is a member of Face Friends Foundation Board of Directors.</v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card style="height: 100%">
          <v-card-title>Member of the Board</v-card-title>
          <v-img src="@/assets/About/Philip.webp" />
          <v-card-text>Phillip Nagheer is a member of Face Friends Foundation Board of Directors.</v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card style="height: 100%">
          <v-card-title>Member of the Board</v-card-title>
          <v-img src="@/assets/About/Kareen.webp" />
          <v-card-text>Kareen Richards is a member of Face Friends Foundation Board of Directors.</v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
name: 'AboutView',
// 这里是组件的JavaScript代码
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