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
  bookedServices: []
}

const mutations = {
  // This is for the expansion panels
  setServicesList(state, services) {
    state.services = services.services
    state.servicesBody = services.servicesBody
  },
  setService(state, service) {
    state.currentAllowedDates = service.currentAllowedDates
    state.bookedServices = service.bookedServices
  }
}

const actions = {
  async showServicesList({ commit }) {
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
  async register({ commit }, userCredentials) {
    try {
      const response = await apiClient.post('register', userCredentials)
      // do not mess up user and username
      const user_name = response.data.user_name
      const token = response.data.access_token
      const refresh_token = response.data.refresh_token
      commit('setUser', { 'user_name': user_name, 'token': token, 'refresh_token': refresh_token })
    } catch (error) {
      console.log(error)
      throw error
    }
  },
  async logout({ commit }) {
    try {
      await apiClient.post('logout')
      commit('logout')
    } catch (error) {
      console.log(error)
      throw error
    }
  }
}

export default { namespaced: true, state, mutations, actions }