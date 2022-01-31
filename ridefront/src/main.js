// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex'
import App from './App'
import router from './router'
import store from './store/index'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import './assets/main.css'
import locale from 'element-ui/lib/locale/lang/en'

Vue.use(ElementUI, { locale });
Vue.use(Vuex);
Vue.config.productionTip = false


/* eslint-disable no-new */
const app = new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>',
  render: h => h(App)
});

// router.beforeEach((to, from, next) => {
//   console.log("here ?")
//   if(to.meta.requireAuth){
//     if(this.$store.state.login){
//       next()
//     }else{
//       console.log("here")
//       next({path:'/'})
//     }
//   }else{
//     next()
//   }
// })

// app.use(store)
