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
  servicesBody: [],
  currentAllowedDates: [],
  currentChosenDate: '',
  bookedServices: []
}

const mutations = {
  // This is for the expansion panels
  setServicesList(state, services) {
    state.services = services.services
    state.servicesBody = services.servicesBody
  },
  setService(state, service) {
    state.bookedServices = service.bookedServices
  },
  setCurrentAllowedDates(state, datesInformation) {
    // An array
    state.currentAllowedDates = datesInformation.currentAllowedDates
  }
}

const actions = {
  async fetchServicesList({ commit }) {
    try {
      // Get services information from API
      const response = await apiClient.get('services')
      // the key in python's storage is username
      const services = response.data.services
      const servicesBody = response.data.servicesBody
      // this notation is like dispatch('login', user)
      commit('setServicesList', { 'services': services, 'servicesBody': servicesBody })
    } catch (error) {
      console.log(error)
      throw error
    }
  },
  async fetchCurrentAllowedDates({ commit }, serviceName) {
    try {
      const response = await apiClient.post('service-current-allowed-dates', serviceName)
      const currentAllowedDates = response.data.currentAllowedDates
      commit('setCurrentAllowedDates', { 'currentAllowedDates': currentAllowedDates })
    } catch (error) {
      console.log(error)
      throw error
    }
  }
}

export default { namespaced: true, state, mutations, actions }