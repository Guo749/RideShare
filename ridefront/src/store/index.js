import Vuex from 'vuex'
import Vue  from 'vue'
import _ from 'lodash'
Vue.use(Vuex)

export default new Vuex.Store({
  state:{
    login: false,
    hasCar: false,
    hitOwn: false,
    hitShare: false,
    hitDriver: false,
    user: {
      id: '',
      username: '',
      email: '',
      password: '',
      car: {
        id: '',
        type: '',
        licensePlateNumber: '',
        capacity: '',
        otherInfo: '',
        owner: '' 
      },
      currentRideDetail: {
        id: '',
        rideOwner: '',
        destAddr: '',
        driverID: '',
        isJoinable: '',
        numPeople: '',
        otherInfo: '',
        shareID: '',
        status: '',
        date: '',
        time: ''
      },
      currentDriverRideDeail: {
        id: '',
        destAddr: '',
        driverID: '',
        isJoinable: '',
        numPeople: '',
        otherInfo: '',
        shareID: '',
        status: '',
        date: '',
        time: ''
      }
    },
    rides: [],
  },
  mutations:{
    flip(state){
      state.login = !state.login
    },
    flipcar(state){
      state.hasCar = !state.hasCar
    },
    setCar(state, carObject) {
      // state.user.car = _.cloneDeep(carObject)
      for (let x in carObject) {
        state.user.car[x] = carObject[x]
      }
    },
    resetCar(state) {
      state.user.car.id = ''
      state.user.car.type = ''
      state.user.car.licensePlateNumber = ''
      state.user.car.capacity = ''
      state.user.car.otherInfo = ''
      state.user.car.owner = ''
    },
    setCurrentRideDetail(state, rideDetail) {
     for (let x in rideDetail) {
        state.user.currentRideDetail[x] = rideDetail[x]
      }
    },
    resetCurrentRideDetail(state) {
      state.user.currentRideDetail.forEach((v)=>state.user.currentRideDetail[v]='')
    },
    setCurrentRideDetailForDriver(state, rideDetail) {
     for (let x in rideDetail) {
        state.user.currentDriverRideDeail[x] = rideDetail[x]
      }
    },
    setHitOwn(state){
      state.hitOwn    = true
      state.hitShare  = false
      state.hitDriver = false
    },
    setHitShare(state){
      state.hitOwn    = false 
      state.hitShare  = true 
      state.hitDriver = false
    },
    setHitDriver(state){
      state.hitOwn    = false
      state.hitShare  = false
      state.hitDriver = true
    }
  }
})