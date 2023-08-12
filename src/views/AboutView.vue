<template>
  <v-container style="margin-top: 12px; margin-bottom: 12px">
    <v-row>
      <v-col>
        <strong>OUR PROGRAMS</strong>
      </v-col>
    </v-row>
    <!--Line1-->
    <!--v-row cols="12" :class="$vuetify.breakpoint.smAndDown ? 'vrow-smAndDown' : 'vrow-normal'"-->
    <v-row v-for="(program, i) in programs" :key="i" style="margin-bottom: 12px; display: flex; justify-content: center;">
      <div v-if="$vuetify.breakpoint.mdAndUp" style="width: 84vw; display: flex; flex-direction: row; justify-content: center">
        <div cols="12" v-if="i % 2 === 0" style="width: 100%; display: flex; flex-direction: row;">
          <div cols="12" sm="12" md="6" lg="6" xl="6" style="width: 50%">
            <v-card>
              <v-img :src=program.source></v-img>
            </v-card>
          </div>
          <div cols="12" sm="12" md="6" lg="6" xl="6" style="width: 50%">
            <div style="height: 100%">
              <div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                <div class="text--title">{{ program.title }}</div>
                <div class="text--body">{{ program.content }}</div>
              </div>
            </div>
          </div>
        </div>
        <div cols="12" v-if="i % 2 === 1" style="width: 98%; display: flex; flex-direction: row;">
          <div cols="12" sm="12" md="6" lg="6" xl="6" style="width: 50%">
            <div style="height: 100%">
              <div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                <div class="text--title">{{ program.title }}</div>
                <div class="text--body">{{ program.content }}</div>
              </div>
            </div>
          </div>
          <div cols="12" sm="12" md="6" lg="6" xl="6" style="width: 50%">
            <v-card>
              <v-img :src=program.source></v-img>
            </v-card>
          </div>
        </div>
      </div>
      <div v-if="$vuetify.breakpoint.smAndDown" style="width: 94vw; display: flex; flex-direction: row; justify-content: center">
        <div style="width: 100%; display: flex; flex-direction: column;">
          <v-card style="width: 100%">
            <v-img :src=program.source style="width: 100%; height: auto"></v-img>
          </v-card>
          <div>
            <div style="height: 100%">
              <div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                <div class="text--title">{{ program.title }}</div>
                <div class="text--body">{{ program.content }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
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
  import apiClient from "@/api.js"
  export default {
    name: 'AboutView',
    // 这里是组件的JavaScript代码
    data() {
      return {
        programs: [],
      }
    },
    mounted() {
      this.initialize()
    },
    methods: {
      initialize() {
        apiClient.get("cms/programs").then(response => {
          this.programs = response.data.programs
        })
      }
    }
  }
</script>

<style scoped>
  /* 这里是关于页面的CSS样式 */
  /*
  .vrow-smAndDown {
    display: flex;
    flex-direction: column-reverse
  }
  .vrow-normal {
    display: flex;
    flex-direction: row
  }
  */
  .text--title {
    text-align: center;
    font-size: 24px
  }

  .text--body {
    text-align: center;
    color: gray
  }
</style>  