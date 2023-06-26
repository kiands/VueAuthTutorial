<template>
  <v-container style="margin-top: 12px; margin-bottom: 12px">
    <v-row style="display: flex; justify-content: center;">
      <v-col>
        <v-card cols="12" style="margin-top: 10px; width: 100%">
          <v-expansion-panels>
            <!--Use v-for here to avoid UI errors-->
            <v-expansion-panel 
              style="width: 100%" @click="showTimeSlots(service)"
              v-for="service in services"
              :key="service"
            >
              <v-expansion-panel-header><strong>{{ service }}</strong></v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-row style="padding-left:20px; padding-right: 20px; display: flex; flex-direction: row; justify-content: space-around;">
                  <v-col style="display: flex; flex-direction: column; justify-content: space-around; align-items: center">
                    <div style="width: 100%; padding-top: 16px; margin-bottom: 20px; margin-right: 20px">
                      <!--Cannot use this.service_descriptions here-->
                      <v-card-text style="font-size: 20px;">{{ service_descriptions[service] }}</v-card-text>
                    </div>
                    <strong style="text-align: center;">
                      Dear visitor: if you need help, please log in to have access to the available dates.
                    </strong>
                    <v-btn @click="showTimeSlots(service)">Show/Refresh Dates</v-btn>
                  </v-col>
                  <!--Mind the format to quote element in objects. `service` is a key here so do not quote with `''`-->
                  <v-col style="display: flex; justify-content: center">
                    <v-date-picker
                      v-model="currentChosenDate"
                      :allowed-dates="allowedDates"
                      class="mt-4"
                      min="2023-01-01"
                      max="2030-01-01"
                    ></v-date-picker>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    v-for="time in dailySlots"
                    :key="time"
                    cols="12" sm="6" md="4" lg="4" xl="4"
                  >
                    <!--Automatically hide when the remaining positions of that time period becomes 0-->
                    <v-card
                      style="display: flex; flex-direction: row; align-items: center"
                      v-if="timeSlots[currentChosenDate][time] > 0"
                    >
                      <v-card-text>{{ time }}</v-card-text>
                      <v-card-text>remaining: {{ timeSlots[currentChosenDate][time] }}</v-card-text>
                      <v-btn style="margin-right: 16px" @click="bookService(service, time)">Book</v-btn>
                    </v-card>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-card
                      v-if="bookedService.service_name !== ''"
                      style="padding: 16px; display: flex; flex-direction: row; justify-content: space-between; align-items: center"
                    >
                      <strong>Current Booking At</strong>
                      <div>{{ bookedService.date }} {{ bookedService.time }}</div>
                      <v-btn @click="revokeBooking(bookedService)">Revoke</v-btn>
                    </v-card>
                  </v-col>
                </v-row>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <!--<v-expansion-panel>
              <v-expansion-panel-header>Panel 2</v-expansion-panel-header>
              <v-expansion-panel-content>
                Some content
              </v-expansion-panel-content>
            </v-expansion-panel>-->
          </v-expansion-panels>
        </v-card>
      </v-col>
    </v-row>
    <!--Board-->
    <v-row style="margin-top:24px">
      <v-col>
        <div>ADDITIONAL PROGRAMS</div>
      </v-col>
    </v-row>
    <v-row style="display: flex; flex-direction: row; justify-content: center">
      <v-col cols="12" sm="6" md="6" lg="4" xl="4">
        <v-card style="height: 100%">
          <v-card-title>International Volunteer</v-card-title>
          <v-img src="@/assets/Services/international.webp" />
          <v-card-text>How would you like to volunteer to serve in Jamaica helping those in need? Well if the answer is "Yes, I would love to volunteer in Jamaica and yet still experience the beauty, the magnificence of its culture, its music, its food, and its wonders", then here is your opportunity! Most, if not all, of your expenses from airfare, to accommodation, to transportation may be tax deductible.</v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="4" xl="4">
        <v-card style="height: 100%">
          <v-card-title>Face Friends Mentors</v-card-title>
          <v-img src="@/assets/Services/mentor.webp" />
          <v-card-text>When you were young, did you know how to study for a test or make plans for college? Do you remember wanting your first car or looking for a part-time job? Simple things that may seem easy or straightforward to you now may be a complete mystery to a young person. 1 in 3 young people will grow up without having a mentor</v-card-text>
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-header>Show More</v-expansion-panel-header>
              <v-expansion-panel-content>either through a formal mentoring program or informally through a family friend or community member leaving them disconnected from a critical resource to help with these very things.</v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-card>
      </v-col>
      <v-col cols="12" sm="6" md="6" lg="4" xl="4">
        <v-card style="height: 100%">
          <v-card-title>NEW EYES GLASSES PROGRAM</v-card-title>
          <v-img src="@/assets/Services/glasses.webp" />
          <v-card-text>New Eyes is expanding its mission and we encourage all health advocates in your state to be made aware of our program so that low-income children and adults can obtain new eyeglasses and the clear vision they need to build better lives. There is NO charge for New Eyes services.  There is no sharing of information. There are no citizenship</v-card-text>
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-header>Show More</v-expansion-panel-header>
              <v-expansion-panel-content>questions. There are no age restrictions.  We operate our program with donated funds to purchase new prescription eyeglasses for people living at 250% or less of the Federal Poverty Guidelines. Children who receive free or reduced-fee school lunches are automatically eligible for our program (and they receive two pairs of glasses each!). We just require that the individual hold a current eye examination prescription (dated within last 24 months). Please spread the word about our service in your community and among your organization!  If you belong to a professional network or Facebook group for organizations that could also use help with free eyeglasses we would urge you to share our details. You may email us with any questions or feedback about our program. We are here to help you in the important work you do – and we are always happy to hear from you!</v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" xl="12"><v-img src="@/assets/Services/background.webp" /></v-col>
      <v-col cols="12" xs="12" md="8">
        <v-card style="display: flex; flex-direction: column; align-items: center">
          <v-card-title>Additional Information</v-card-title>
          <v-card-text>The need for food security in Sugar Hill Georgia and Saint Mary Jamaica and the wider Georgia and Jamaican communities are not just great but urgent, since this devastating Covid 19 pandemic many families who would not otherwise need food assistance find themselves in need of food to feed their families. Face Friends Foundation are looking for grocery stores, food suppliers to come on board and donate fresh food, dry foods and canned food. We are also looking for frozen foods, fresh meats and vegetables, bottled water and juices. Please call us at 678-765-0482 and tell us how you can help.</v-card-text>
          <v-card-text>So you may be wondering, what are some of the items you can donate? Here is a list of our needs: shelf-stable items such as cereal, lentils, rice, canned vegetables, macaroni & cheese boxes, canned meats, dried or canned beans, pasta, and canned and soups. We also accept fresh items such as proteins like chicken, beef, pork, goat, fish, and lamb, dairy products, fresh fruits and vegetables, bakery goods, and lots more-just ask us.</v-card-text>
          <v-card-text>The Face Friends Foundation Incorporated was established to meet the short term needs specifically of the residents of Georgia and Jamaica. If you can donate items, please call us at 678-765-0482 for our Georgia office or 876-677-9019 for the Jamaican office and we will point you in the right direction. If you are living in Jamaica and need services we are opened Mondays between 6pm-8pm, Thursdays between 11am-2pm and Saturday 11am-4pm.</v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" xs="12" md="4">
        <v-card style="padding-bottom: 24px; height: 100%; display: flex; flex-direction: column; align-items: center">
          <v-card-title>Learn More</v-card-title>
          <v-card-text>Face Friends Foundation Incorporated will have three major programs every year: first our Annual Easter Bun and Cheese Box, second our Summer Backpack and School Supplies Giveaway, and lastly our  Holiday Dinner Food Box, so don’t forget to register for these programs.</v-card-text>
          <v-btn>Find Out More</v-btn>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
</style>

<script>
// May not be used if no need to test functions
// import apiClient from "@/api.js"

export default {
  name: 'ServicesView',
  // 这里是组件的JavaScript代码
  data: () => ({
    timeSlots: '',
    dailySlots: [], // This only exists in ServicesView.
    services: [],
    service_descriptions: {},
    currentChosenDate: '',
    bookedService: { 'service_name': '' },
  }),

  created() {
    // When this view is loaded, whatever first time or refresh, call the API and load the main list.
    this.showServicesList()
  },

  watch: {
    // 每当 currentChosenDate 改变时，这个函数就会执行
    currentChosenDate(newVal, oldVal) {
      // 在这里调用你想要执行的函数
      this.updateDailySlots(newVal)
    }
  },

  methods: {
    showServicesList: function() {
      // This is async and we need to wait for $store to be modified or v-for will be empty
      this.$store.dispatch('service/fetchServicesList').then(() => {
        this.services = this.$store.state.service.services
        this.service_descriptions = this.$store.state.service.service_descriptions
      })
    },
    /*
      I will use the `key` in v-for to access each service's allowed dates.
      In this data picker component, each time the expansion panel was clicked, the allowed dates
      can be updated. After the update, the `:allowedDates` will check new data and update the view.
      Remember that in some primitive implementations, changes in data will not always reflect in the view.
      The time slots may need the `watch` feature to monitor the change of selected data and do update.
    */
    showTimeSlots: function(service) {
      // console.log(service) // The formal implementation will be an api call that uses this parameter
      /*
        Use vue to call the API to get current service's allowed dates.
        The payload of dispatch should use JS object notation. It can be read as json on backend.
      */
      this.currentChosenDate = ''; // Each time the user clicks another service, clear existed currentChosenDate.
      if (this.$store.state.auth.isLoggedIn === true) {
        this.$store.dispatch('service/fetchTimeSlots', { 'service_name': service }).then(() => {
          this.timeSlots = this.$store.state.service.timeSlots
        })
        // Fetch booked service to help with blocking illegal access like multiple booking.
        this.$store.dispatch('service/fetchBookedService', { 'user_id': this.$store.state.auth.user_id, 'service_name': service }).then(() => {
          this.bookedService = this.$store.state.service.bookedService
        })
      } else {
        console.log('only show basic information')
      }
    },

    /*
      The allowedDates property of vuetify date picker is a method to check each date the component
      passes. For example: allowed dates are even dates:
      allowedDates: val => parseInt(val.split('-')[2], 10) % 2 === 0
    */
    allowedDates: function(val) {
      // Do not pass currentAllowedDates to this function because vue will not do this, use `this.` -- ChatGPT
      return Object.keys(this.timeSlots).includes(val)
    },

    // When the dates on the calendar is clicked, this function will be triggered.
    updateDailySlots(date) {
      // This if-else is designed for clearing old service's dailySlots when the user clicks a new service.
      if (date === '') {
        this.dailySlots = []
      } else {
        this.dailySlots = Object.keys(this.timeSlots[date])
        // console.log(this.dailySlots)
      }
    },

    bookService(service, time) {
      if (this.bookedService['service_name'] === '') {
        this.$store.dispatch('service/bookService', { 'user_id': this.$store.state.auth.user_id, 'service_name': service, 'date': this.currentChosenDate, 'time': time }).then(() => {
          // Update time slots when a service is booked
          this.timeSlots = this.$store.state.service.timeSlots
          // Then update daily slots
          this.updateDailySlots(this.currentChosenDate)
          // Finally, update newest booked service
          this.bookedService = this.$store.state.service.bookedService
        })
      } else {
        console.log('Sorry, you already have an existed booking')
      }
    },

    revokeBooking(bookedService) {
      this.$store.dispatch('service/revokeBooking', { 'user_id': this.$store.state.auth.user_id, 'service_name': bookedService.service_name, 'date': bookedService.date, 'time': bookedService.time }).then(() => {
        // Update time slots when a service is booked
        this.timeSlots = this.$store.state.service.timeSlots
        // Then update daily slots
        this.updateDailySlots(this.currentChosenDate)
        // Finally, update newest booked service
        this.bookedService = this.$store.state.service.bookedService
      })
    }
  },
}
</script>