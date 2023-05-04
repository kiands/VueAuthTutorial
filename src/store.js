// the benefits of using vuex:
// 1. Store and maintain data centrally.
// 2. just focus on accessing the API and dispatch once, the remaining things can be pre defined and reused.
import Vuex from 'vuex'
import auth from './auth'

const store = new Vuex.Store({
  modules: {
    auth
  }
})

export default store