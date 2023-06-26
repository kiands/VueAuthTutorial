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
  bookedService: { 'service_name': '' }
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
  setBookedService(state, service) {
    state.bookedService = service.bookedService
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
      // If the value of the payload is a string, we need JSON.parse(). If it was a JSON in backend, there's no need.
      const timeSlots = response.data.timeSlots
      commit('setTimeSlots', { 'timeSlots': timeSlots })
    } catch (error) {
      console.log(error)
      throw error
    }
  },
  async fetchBookedService({ commit }, serviceInformation) {
    try {
      const response = await apiClient.post('booked_service', serviceInformation)
      // If the value of the payload is a string, we need JSON.parse(). If it was a JSON in backend, there's no need.
      const bookedService = response.data.bookedService
      commit('setBookedService', { 'bookedService': bookedService })
    } catch (error) {
      console.log(error)
      throw error
    }
  },
  async bookService({ commit }, serviceInformation) {
    try {
      // Post and book, then whatever the result is, we need to update the time slots using the response data.
      const response = await apiClient.post('book_service', serviceInformation)
      const timeSlots = response.data.timeSlots
      const bookedService = response.data.bookedService
      // Set new time slots
      commit('setTimeSlots', { 'timeSlots': timeSlots })
      // Set booked service
      commit('setBookedService', { 'bookedService': bookedService })
    } catch (error) {
      console.log(error)
      throw error
    }
  },
  async revokeBooking({commit}, serviceInformation) {
    try {
      // Post and revoke, then whatever the result is, we need to update the time slots using the response data.
      const response = await apiClient.post('revoke_booking', serviceInformation)
      const timeSlots = response.data.timeSlots
      // Set updated time slots
      commit('setTimeSlots', { 'timeSlots': timeSlots })
      // Set booked service as 'empty'
      commit('setBookedService', { 'bookedService': { 'service_name': '' } })
    } catch (error) {
      console.log(error)
      throw error
    }
  }
}

export default { namespaced: true, state, mutations, actions }