import Vue from 'vue'
import Vuex from 'vuex'
import apiClient from "@/api.js"

Vue.use(Vuex)

/*
  // Initialize data from page refresh
  let user_name = localStorage.getItem("user_name") || '';
  let token = localStorage.getItem("token") || '';
  let refresh_token = localStorage.getItem("refresh_token") || '';
  let isLoggedIn = localStorage.getItem("isLoggedIn") || false;
*/

const state = {
  services: [],
  service_descriptions: {},
  timeSlots: '',
  currentChosenDate: '',
  bookedServices: []
}

const mutations = {
  // This is for the expansion panels
  setServicesList(state, services) {
    state.services = services.services
    state.service_descriptions = services.service_descriptions
  },
  setTimeSlots(state, datesInformation) {
    // An array
    state.timeSlots = datesInformation.timeSlots
  },
  setBookedServices(state, service) {
    state.bookedServices = service.bookedServices
  }
}

const actions = {
  async fetchServicesList({ commit }) {
    try {
      // Get services information from API
      const response = await apiClient.get('services')
      // the key in python's storage is username
      const services = response.data.services
      // Flask automatically parsed this into JSON. Has something different with things in `fetchTimeSlots()`
      const service_descriptions = response.data.service_descriptions
      // this notation is like dispatch('login', user)
      commit('setServicesList', { 'services': services, 'service_descriptions': service_descriptions })
    } catch (error) {
      console.log(error)
      throw error
    }
  },
  async fetchTimeSlots({ commit }, serviceName) {
    try {
      const response = await apiClient.post('service_time_slots', serviceName)
      // The specific received data should be parsed or it is not a JS object
      const timeSlots = JSON.parse(response.data.timeSlots)
      commit('setTimeSlots', { 'timeSlots': timeSlots })
    } catch (error) {
      console.log(error)
      throw error
    }
  }
}

export default { namespaced: true, state, mutations, actions }