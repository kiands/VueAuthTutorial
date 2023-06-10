<template>
  <v-container style="margin-top: 12px; margin-bottom: 12px">
    <v-row>
      <v-col style="width: 80vw; display: flex; flex-direction: column; align-items: center">
        <v-text-field
          v-model="name"
          style="width: 100%"
          label="Name"
          :rules="rules4name"
          hide-details="auto"
        ></v-text-field>
        <v-text-field
          v-model="email"
          style="width: 100%"
          label="Email"
          :rules="rules4email"
          hide-details="auto"
        ></v-text-field>
        <v-text-field
          v-model="source"
          style="width: 100%"
          label="Where did you heard about us?"
          :rules="rules4source"
          hide-details="auto"
        ></v-text-field>
        <v-text-field
          v-model="reason"
          style="width: 100%"
          label="Why are you contacting us today?"
          :rules="rules4reason"
          hide-details="auto"
        ></v-text-field>
        <v-text-field
          v-model="additional_information"
          style="width: 100%"
          label="Is there any additional questions you would like to provide?"
          :rules="rules4additional_information"
          hide-details="auto"
        ></v-text-field>
        <v-btn style="margin-top: 24px; margin-bottom: 24px" @click="submit()">Submit</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import apiClient from "@/api.js"
  export default {
    name: 'ContactView',
    // 这里是组件的JavaScript代码
    data() {
      return {
        rules4name: [
          value => !!value || 'Required.',
          value => (value || '').length <= 45 || 'Please enter no more than 45 characters~'
        ],
        rules4email: [
          value => !!value || 'Required.',
          value => {
            const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            return pattern.test(value) || 'Invalid e-mail.'
          },
          value => (value || '').length <= 45 || 'Please enter no more than 45 characters~'
        ],
        rules4source: [
          value => !!value || 'Required.',
          value => (value || '').length >= 3 || 'Please enter no less than 3 characters~',
          value => (value || '').length <= 45 || 'Please enter no more than 45 characters~'
        ],
        rules4reason: [
          value => !!value || 'Required.',
          value => (value || '').length >= 3 || 'Please enter no less than 3 characters~',
          value => (value || '').length <= 255 || 'Please enter no more than 255 characters~'
        ],
        rules4additional_information: [
          value => (value || '').length <= 255 || 'Please enter no more than 255 characters~'
        ],
        name: '',
        email: '',
        source: '',
        reason: '',
        additional_information: ''
      }
    },
    methods: {
      async submit() {
        if (this.name !== '' && this.email !== '' && this.source !== '' && this.reason !== '') {
          await apiClient.post('contact', {
            'name': this.name,
            'email': this.email,
            'source': this.source,
            'reason': this.reason,
            'additional_information': this.additional_information
          }).then(response => {
            // Handle success here
            // response.data will contain the response data from the server
            console.log('Success:', response.data)
            // You can also use response.data to perform other actions, e.g. alert the user
            // alert("Data successfully sent!")
          }).catch(error => {
            // Handle error here
            console.log('Error:', error)
            // You can also use error.message to perform other actions, e.g. alert the user
            alert("There was an error sending the data.")
          })
        } else {
          console.log('please fill in required information');
        }
      }
    }
  }
</script>

<style scoped>
  /* 这里是关于页面的CSS样式 */
</style>  