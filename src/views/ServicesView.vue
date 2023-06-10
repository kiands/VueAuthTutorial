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
              <v-expansion-panel-header>{{ service }}</v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-row style="padding-left:20px; padding-right: 20px; display: flex; flex-direction: row; justify-content: center;">
                  <div style="width:290px; padding-top: 16px; margin-bottom: 20px; margin-right: 20px">
                    <v-btn>
                    </v-btn>
                  </div>
                  <!--Mind the format to quote element in objects. `service` is a key here so do not quote with `''`-->
                  <v-date-picker
                    v-model="currentChosenDate"
                    :allowed-dates="allowedDates"
                    class="mt-4"
                    min="2023-01-01"
                    max="2030-01-01"
                  ></v-date-picker>
                </v-row>
                <v-row>
                  <v-card>
                    <v-card-text>Time Slots</v-card-text>
                  </v-card>
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
  </v-container>
</template>

<style scoped>
</style>

<script>
import apiClient from "@/api.js" // May not be used if no need to test functions

export default {
  name: 'ServicesView',
  // 这里是组件的JavaScript代码
  data: () => ({
    timeSlots: '',
    services: [],
    // servicesBody: {},
    currentChosenDate: '',
    bookedServices: { "title": "Food Support" },
  }),

  created() {
    // When this view is loaded, whatever first time or refresh, call the API and load the main list.
    this.showServicesList()
  },

  methods: {
    showServicesList: function() {
      // This is async and we need to wait for $store to be modified or v-for will be empty
      this.$store.dispatch('service/fetchServicesList').then(() => {
        this.services = this.$store.state.service.services
        // this.servicesBody = this.$store.state.service.servicesBody
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
      console.log(service) // The formal implementation will be an api call that uses this parameter
      /*
        Use vue to call the API to get current service's allowed dates.
        The payload of dispatch should use JS object notation. It can be read as json on backend.
      */
      this.$store.dispatch('service/fetchTimeSlots', { 'service': service }).then(() => {
        this.timeSlots = this.$store.state.service.timeSlots
      })
    },

    /*
      The allowedDates property of vuetify date picker is a method to check each date the component
      passes. For example: allowed dates are even dates:
      allowedDates: val => parseInt(val.split('-')[2], 10) % 2 === 0
    */
    allowedDates: function(val) {
      // Do not pass currentAllowedDates to this function because vue will not do this, use `this.` -- ChatGPT
      return Object.keys(this.timeSlots).includes(val)
    }
  },
}
</script>