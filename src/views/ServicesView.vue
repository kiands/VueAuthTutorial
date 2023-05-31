<template>
  <v-container>
    <v-row style="display: flex; justify-content: center;">
      <v-card cols="12" style="margin-top: 10px; width: 80%">
        <v-expansion-panels
          multiple
        >
          <v-expansion-panel style="width: 100%">
            <v-expansion-panel-header>Food Support</v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-row style="padding-left:20px; padding-right: 20px; display: flex; flex-direction: row; justify-content: center;">
                <div style="width:290px; padding-top: 16px; margin-bottom: 20px; margin-right: 20px">
                  <v-btn>
                  </v-btn>
                </div>
                <v-date-picker
                  v-model="date"
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

          <v-expansion-panel>
            <v-expansion-panel-header>Panel 2</v-expansion-panel-header>
            <v-expansion-panel-content>
              Some content
            </v-expansion-panel-content>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-header>Panel 3</v-expansion-panel-header>
            <v-expansion-panel-content>
              Some content
            </v-expansion-panel-content>
          </v-expansion-panel>
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
      date: '',
    }),

    methods: {
      allowedDates: val => parseInt(val.split('-')[2], 10) % 2 === 0,
    },
  }
</script>