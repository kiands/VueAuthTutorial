import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const state = {
  user: null,
  token: localStorage.getItem('token') || '',
  isLoggedIn: false
}

const mutations = {
  // the parameter user here is an object
  setUser(state, user) {
    console.log(user)
    state.user = user.user_name
    state.token = user.token
    state.isLoggedIn = true
    // localStorage
    localStorage.setItem('token', user.token)
  },
  logout(state) {
    state.user = null
    state.token = ''
    state.isLoggedIn = false
    localStorage.removeItem('token')
  }
}

const actions = {
  async login({ commit }, userCredentials) {
    try {
      if (userCredentials.oauth) {
        console.log("OK")
        commit('setUser', { 'user_name': userCredentials.user_name, 'token': userCredentials.token });
      } else {
        const response = await axios.post('login', userCredentials)
        // the key in python's storage is username
        const user_name = response.data.user_name
        const token = response.data.access_token
        // this notation is like dispatch('login', user)
        commit('setUser', { 'user_name': user_name, 'token': token });
      }
    } catch (error) {
      console.log(error)
      throw error
    }
  },
  async register({ commit }, userCredentials) {
    try {
      const response = await axios.post('register', userCredentials)
      // do not mess up user and username
      const user_name = response.data.user_name
      const token = response.data.access_token
      commit('setUser', { 'user_name': user_name, 'token': token })
    } catch (error) {
      console.log(error)
      throw error
    }
  },
  async logout({ commit }) {
    try {
      await axios.post('logout')
      commit('logout')
    } catch (error) {
      console.log(error)
      throw error
    }
  }
}

export default { namespaced: true, state, mutations, actions }