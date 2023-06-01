<template>
  <v-container>
    <v-row style="display: flex; justify-content: center;">
      <v-card cols="12" style="margin-top: 10px; width: 80%">
        <v-expansion-panels
          accordion
          v-for="service in services"
          :key="service"
        >
          <v-expansion-panel style="width: 100%" @click="fetchAllowedDates(service)">
            <v-expansion-panel-header>{{ service }}</v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-row style="padding-left:20px; padding-right: 20px; display: flex; flex-direction: row; justify-content: center;">
                <div style="width:290px; padding-top: 16px; margin-bottom: 20px; margin-right: 20px">
                  <v-btn>
                  </v-btn>
                </div>
                <!--Mind the format to quote element in objects. `service` is a key here so do not quote with `''`-->
                <v-date-picker
                  v-model=servicesBody[service].chosenDate
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
    </v-row>
  </v-container>
</template>

<style scoped>
</style>

<script>
  export default {
    name: 'ServicesView',
    // 这里是组件的JavaScript代码
    data: () => ({
      currentAllowedDates: [],
      services: ['Food Support', 'Tutor Support'],
      servicesBody: {
        "Food Support": {"title": "Food Support", "chosenDate": '2023-06-22' },
        "Tutor Support": {"title": "Tutor Support", "chosenDate": '2023-06-02' }
      }
    }),

    methods: {
      // I will use the `key` in v-for to access each service's allowed dates
      fetchAllowedDates: function(service) {
        console.log(service) // The formal implementation will be an api call that uses this parameter
        this.currentAllowedDates = ['2023-06-02', '2023-06-03', '2023-06-22']
      },

      /*
        The allowedDates property of vuetify date picker is a method to check each date the component
        passes. For example: allowed dates are even dates:
        allowedDates: val => parseInt(val.split('-')[2], 10) % 2 === 0
      */
      allowedDates: function(val) {
        // Do not pass currentAllowedDates to this function because vue will not do this, use `this.` -- ChatGPT
        return this.currentAllowedDates.includes(val)
      }
    },
  }
</script>