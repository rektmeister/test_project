// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from 'element-ui'
import VueAMap from 'vue-amap'
import 'element-ui/lib/theme-chalk/index.css'
import fullCalendar from 'vue-fullcalendar'
import mavonEditor from 'mavon-editor'
import io from 'socket.io-client';
// import socketIO from 'socket.io-client'
import 'normalize.css/normalize.css'
import 'mavon-editor/dist/css/index.css'
import App from './App'
import router from './router'
import Toast from './components/toast/main.js'
import axios from './api'
import store from './store'
import directives from './directives'
import { VueAMapKey } from '@/const'
// import './../static/css/base.css'
import './../static/css/base.scss'
import './../static/css/var.scss'
import './../static/css/theme.scss'

Vue.use(ElementUI)
Vue.use(VueAMap)
Vue.use(mavonEditor)
Vue.component('full-calendar', fullCalendar)
// 初始化vue-amap
VueAMap.initAMapApiLoader({
  // 高德的key
  key: VueAMapKey,
  // 插件集合
  plugin: ['AMap.Autocomplete', 'AMap.PlaceSearch', 'AMap.Scale', 'AMap.OverView', 'AMap.ToolBar', 'AMap.MapType', 'AMap.PolyEditor', 'AMap.CircleEditor'],
  // 高德 sdk 版本，默认为 1.4.4
  v: '1.4.4'
});

// // socket连接
// Vue.use(new VueSocketIO({
//   // debug: true,
//   connection: process.env.SOCKET_URL,
//   // vuex: {
//   //   store,
//   //   actionPrefix: "SOCKET_",
//   //   mutationPrefix: "SOCKET_"
//   // }
// }))

// 注册全局指令
Object.keys(directives).forEach(i => Vue.directive(i, directives[i]))

Vue.config.productionTip = false
Vue.prototype.$toast = Toast
Vue.prototype.$http = axios
Vue.prototype.$eventBus = new Vue()

const socket = io(process.env.SOCKET_URL, { transports: ["websocket"] });
Vue.prototype.$socket = socket;

var publicKey = "-----BEGIN RSA PUBLIC KEY-----\
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4fkcgY3jk2Fi/sbFq2bZNQ5I9CHDchj5i781Dr3ckK2c82nuUj+2LHZmAr3vcBfywfoZV6XA9CuVSPssK4SqCJz/05pZ4nzGFBnquQEWS5jl5PsZYaVDhtQaSoXVbrMOECEJpfm0NDavuOtK2O4R/5cLWyM2sg/eG6JbiHF7w5+l8D5lO7O/VOLUD2NQMfBRVeyDmoCR3eg4+sf70t9VEzQiEpW5dYNLh8p/6iPYMEGMDnICyqnaL/y5jC4rXqRjCoKL+JbpEs9EUc2Z6ZaaZ9dTyT7siXZcfs1+VkpLYxRjuxlDPSd2YP1GfykQN3oQkG56PFe33DBG2zFOpw0jTQIDAQAB\
-----END RSA PUBLIC KEY-----\
"

var privateKey = "-----BEGIN RSA PRIVATE KEY-----\
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDh+RyBjeOTYWL+xsWrZtk1Dkj0IcNyGPmLvzUOvdyQrZzzae5SP7YsdmYCve9wF/LB+hlXpcD0K5VI+ywrhKoInP/TmlnifMYUGeq5ARZLmOXk+xlhpUOG1BpKhdVusw4QIQml+bQ0Nq+460rY7hH/lwtbIzayD94boluIcXvDn6XwPmU7s79U4tQPY1Ax8FFV7IOagJHd6Dj6x/vS31UTNCISlbl1g0uHyn/qI9gwQYwOcgLKqdov/LmMLitepGMKgov4lukSz0RRzZnplppn11PJPuyJdlx+zX5WSktjFGO7GUM9J3Zg/UZ/KRA3ehCQbno8V7fcMEbbMU6nDSNNAgMBAAECggEBAOBtqhsdkbVxVoGVZwLZjcY83sXgtp0eItHhYE+4z1O9qhCy16hGcKbuHFiCzUg18Lsoqny7Oc0HcCfglbjO9JTDYO2G8diYdZ3HM7D0XHFOdJ0bqdSp70v8YfQ7wYNFQCVSuqNmQcxNt+5feaHDqIqBOB0W9x6X1c76TBBSLUpV6Vcib0CBfNa22Okpok1aHAq7z1ejaNpuoQcM3jiIFMGHx5bxQ0iJOSQAOwMIJwHqpYhXxDjuLNPFfIND5V5ERxBmFOQK2q0NeeNk8FAmSVRMjU+xKz0buAK2TgNa4ZVyGrL+sYO4mA0bPtoIqo1WNPh+9uYrV+1YX4u0omO0270CgYEA/lbnL/qevqNOZWn0ERjNqemR8SpiVQAtV+ua6FmF9CG5bNJYk73DvrtvyUohy24LyorGRGJF+83Q6oJWOMx7Yfeo7VlsZcegdQo6ChuJdN5nd8apwTAZ0+WNKIQnQBGGHhm9cBwfn+tZQH5EiHHqlF85NnEg1T86nLLhrWLquGcCgYEA43LMIgeS2RY4eXRL5ust/9bkv6GU2n0csWRDwMyXbP7poM7SQdoS+swzEmT70tkF75EX4ak/uIIXOtJKigZzaarNzLF8wi8WmhHL1Fikimf6jpQi1sluQm5NBkCK7cWjRigt11PyoqqBB/IBA+xWb0TwyNNd4JnBxag/15qsRisCgYEAkeqLojQXpOmODZK26qQfQe71wrV9SqTaXsmVyt2pg0Fh3zPii4hgZ+mjHYmBT/OnoiDx1MPIwMj4pcH284kk9DSg3uLh1Jat0Nf4KlpYBwudstLwCxyshKv6yxbeadxj5JsB2vLXlejxAJYwfVNVsJ/c9AX9PzqSRto9rTrFzNsCgYEAqjdBWb49QcWFYi+MljYu6KZT7q3oDlNPY9pbcjAqquFiynu9kpa3WYX0OrHkW/kanh0BuFnHXDfPVrAGJKGLQesXtTam3VQMICVtW28zRHloY8etAv0gTQrrDeDDmAoulNSA6gLjNKVRhzavV9ZJIWCAqmq0eN/YyimODbatcp0CgYBEhaaQmglYjgmdnF4yZCKTDRW2LFyHbVvDAcigrIfg0FSSEreFvpZS/OzDNBcpL1tOomv63W5NAjmbmsouC1U1xlTIyI/vdKAGQdpmWimAxfimyCXxNv9iot1sz3dyc7eeQyfzg+aAW0t7WqbeqwcyyO5ouHM3OkG5u6ycCdOWBg==\
-----END RSA PRIVATE KEY-----"

import JSEncrypt from 'jsencrypt'

Vue.prototype.$rsa_encrypt = function (str) {
  str = encodeURI(str)
  // 如果是对象/数组的话，需要先JSON.stringify转换成字符串
  let jsencrypt = new JSEncrypt();
  jsencrypt.setPublicKey(publicKey);
  let result = jsencrypt.encrypt(str);
  return result
};

Vue.prototype.$rsa_decrypt = function (str) {
  let jsencrypt = new JSEncrypt();
  jsencrypt.setPrivateKey(privateKey);
  let result = jsencrypt.decrypt(str);
  result = decodeURI(result)
  return result
};


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  // components: { App },
  // template: '<App/>'
  render: h => h(App)
}).$mount('#app')
