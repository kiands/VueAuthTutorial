// the benefits of using vuex:
// 1. Store and maintain data centrally.
// 2. just focus on accessing the API and dispatch once, the remaining things can be pre defined and reused.
import Vuex from 'vuex'
import auth from './auth'
import service from './service'

const store = new Vuex.Store({
  modules: {
    auth,
    service
  }
})

export default store