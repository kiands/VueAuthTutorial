// the benefits of using vuex:
// 1. Store and maintain data centrally.
// 2. just focus on accessing the API and dispatch once, the remaining things can be pre defined and reused.

import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = 'http://localhost:5000/api/'

const store = new Vuex.Store({
  state: {
    user: null,
    isLoggedIn: false
  },
  // the methods about commit operation
  mutations: {
    setUser(state, user) {
      state.user = user
      state.isLoggedIn = true
    },
    logout(state) {
      state.user = null
      state.isLoggedIn = false
    }
  },
  // the methods about dispatch operation
  // to access the methods in actions from components/views: this.$store.dispatch(method_name)
  actions: {
    async login({ commit }, userCredentials) {
      try {
        const response = await axios.post(API_URL + 'login', userCredentials)
        // the key in python's storage is username
        const user = response.data.username
        // this notation is like dispatch('login', user)
        commit('setUser', user)
      } catch (error) {
        console.log(error)
        throw error
      }
    },
    async register({ commit }, userCredentials) {
      try {
        const response = await axios.post(API_URL + 'register', userCredentials)
        const user = response.data.user
        commit('setUser', user)
      } catch (error) {
        console.log(error)
        throw error
      }
    },
    async logout({ commit }) {
      try {
        await axios.post(API_URL + 'register')
        commit('logout')
      } catch (error) {
        console.log(error)
        throw error
      }
    }
  }
})

export default store