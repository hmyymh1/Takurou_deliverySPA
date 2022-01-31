import { createStore } from 'vuex'

import cartShow from './cartShow'
import cartList from './cartList'
import userStore from './userStore'

export default createStore({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    cartShow,
    cartList,
    userStore,
  }
})
