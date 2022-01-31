import Vue from 'vue'
import Router from 'vue-router'
import createuser    from '@/components/createuser'
import login         from '@/components/login'
import leftnav       from '@/components/leftnav'
import registercar   from '@/components/registercar'
import dashboard     from '@/components/dashboard'
import startride     from '@/components/startride'
import joinride      from '@/components/joinride'
import ridedetail    from '@/components/ridedetail'
import personinfo    from '@/components/personinfo'
import orderForDriver from '@/components/orderForDriver'
import rideDetailForDriver from '@/components/rideDetailForDriver'
import mixedorder    from '@/components/mixedorder' 
import mysharedorder from '@/components/mysharedorder'  
import myownorder    from '@/components/myownorder'
import availableorder from '@/components/availableorder'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/createuser/',
      name: 'createuser',
      component: createuser
    },

    {
      path: '/myownorder/',
      name: 'myownorder',
      component:myownorder 
    },

    {
      path: '/mysharedorder/',
      name: 'mysharedorder',
      component:mysharedorder 
    },
    {
      path: '/availableorder/',
      name: 'availableorder',
      component: availableorder
    },

    {
      path: '/mixedorder/',
      name: 'mixedorder',
      component: mixedorder 
    },

    {
      path: '/orderForDriver/',
      name: 'orderForDriver',
      component: orderForDriver
    },

    {
      path: '/ridedetail/',
      name: 'ridedetail',
      component: ridedetail
    },


    {
      path: '/startride',
      name: 'startride',
      component: startride,
    },

    {
      path: '/joinride',
      name: 'joinride',
      component: joinride
    },

    {
      path: '/',
      name: 'login',
      component: login
    },

    {
      path: '/leftnav',
      name: 'leftnav',
      component: leftnav
    },

    {
      path: '/registercar',
      name: 'registercar',
      component: registercar
    },

    {
      path: '/dashboard',
      name: 'dashboard',
      component: dashboard      
    },

    {
      path: '/personinfo',
      name: 'personinfo',
      component: personinfo      
    },
    {
      path: '/rideDetailForDriver',
      name: 'rideDetailForDriver',
      component: rideDetailForDriver
    },
  ]
})
