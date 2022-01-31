import axiosInstance from './index'

const axios = axiosInstance
axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'
export const editUser = (username, email, id) => {
    return axios.put(`edituser/${id}`,
        {'username': username, 'email': email})
}

export const postUser = (username, password, email) => {
    return axios.post('register',
        { 'username': username, 'password': password, 'email': email })
}

export const loginUser = (username, password) => {
    return axios.post('login',
        { 'username': username, 'password': password })
}

export const logoutUser = (username) => {
    return axios.get('logout',
    {})
}

/////////car zone /////////////////


export const getCar = () => {
    return axios.get('carList/')
}

export const loadCar = () => {
    return axios.get('carList/')
}

export const loadMyOwnRide = (id) => {
    return axios.get(`getOwnList/${id}`)
}

export const loadSharedRide = (id) => {
    return axios.get(`getSharedList/${id}`)
}

export const loadOpenRide = (id) => {
    return axios.get(`getOpenList/${id}`)
}



export const cancelRide = (id) => {
    return axios.put(`cancelRide/${id}`,
    {'shareID': ''})
}

export const getDriverByFk = (fk) => {
    return axios.get(`user/${fk}`)
}

export const getCarByFk = (fk) => {
    return axios.get(`carListByFk/${fk}`)
}

export const registercar = (type, platenum, capacity, otherinfo) => {
    return axios.post('carList/',
        { 'type': type, 'licensePlateNumber': platenum, 'capacity': capacity, 'otherInfo': otherinfo })
}

export const editcar = (type, platenum, capacity, otherinfo, id) => {
    return axios.put(`carList/${id}`,
        { 'type': type, 'licensePlateNumber': platenum, 'capacity': capacity, 'otherInfo': otherinfo })
}

export const delcar = (id) => {
    return axios.delete(`carList/${id}`,
        {})
}

/////////// ride zone ////////////////////////////////


export const loadRideList = () => {
    return axios.get('rideList/')
}
export const postride = (destAddr, arrivalDate, arrivalTime, numPeople, isJoinable, otherInfo) => {
    return axios.post('rideList/',
        { 'destAddr': destAddr, 'date': arrivalDate, 'time': arrivalTime, 'numPeople': numPeople, 'isJoinable': isJoinable, 'otherInfo': otherInfo })
}

export const editride = (
    destAddr, 
    arrivalDate, 
    arrivalTime,
    numPeople, 
    isJoinable, 
    otherInfo, 
    id) => {
    return axios.put(`rideList/${id}`,
        {
            'destAddr': destAddr,
            'date': arrivalDate,
            'time': arrivalTime,
            'numPeople': numPeople,
            'isJoinable': isJoinable,
            'otherInfo': otherInfo,
        })
}

export const joinride = (rideid, shareID) => {
    return axios.put(`rideList/${rideid}`,
    {'shareID':shareID})
}
export const claimride = (rideid, driverID) => {
    return axios.put(`rideList/${rideid}`,
    {'driverID':driverID, 'status':2})
}

export const completeride = (rideid) => {
    return axios.put(`completeRide/${rideid}`,
    {'status': 3})
}

export const deleride = (id) => {
    return axios.delete(`rideList/${id}`,
        {})
}

export const driverFilteredRides = () => {
    return axios.get('driverFilteredRides/')
}


export const driverConfirmedRides = () => {
    return axios.get('driverConfirmedRides/')
}