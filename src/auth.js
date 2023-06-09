import Vue from 'vue'
import Vuex from 'vuex'
import apiClient from "@/api.js"

Vue.use(Vuex)

// Initialize data from page refresh
let user_id = localStorage.getItem("user_id") || '';
let user_name = localStorage.getItem("user_name") || '';
let token = localStorage.getItem("token") || '';
let refresh_token = localStorage.getItem("refresh_token") || '';
let isLoggedIn = localStorage.getItem("isLoggedIn") || false;

const state = {
  user_id: user_id,
  user_name: user_name,
  token: token,
  refresh_token: refresh_token,
  isLoggedIn: isLoggedIn,
}

const mutations = {
  // the parameter user here is an object
  setUser(state, user) {
    state.user_id = user.user_id
    state.user_name = user.user_name
    state.token = user.token
    state.refresh_token = user.refresh_token
    state.isLoggedIn = true
    // Use localStorage to survive data from page refresh
    localStorage.setItem('user_id', user.user_id)
    localStorage.setItem('user_name', user.user_name)
    localStorage.setItem('token', user.token)
    localStorage.setItem('refresh_token', user.refresh_token)
    localStorage.setItem('isLoggedIn', true)
  },
  logout(state) {
    state.user_id = ''
    state.user_name = ''
    state.token = ''
    state.refresh_token = ''
    state.isLoggedIn = false
    localStorage.removeItem('user_id')
    localStorage.removeItem('user_name')
    localStorage.removeItem('token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('isLoggedIn')
  }
}

const actions = {
  async login({ commit }, userCredentials) {
    try {
      const response = await apiClient.post('login', userCredentials)
      // the key in python's storage is username
      const user_id = response.data.user_id
      const user_name = response.data.user_name
      const token = response.data.access_token
      const refresh_token = response.data.refresh_token
      // this notation is like dispatch('login', user)
      commit('setUser', { 'user_id': user_id, 'user_name': user_name, 'token': token, 'refresh_token': refresh_token })
    } catch (error) {
      console.log(error)
      throw error
    }
  },
  // did not finish, need to add user_id feature
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