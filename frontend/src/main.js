import { createApp } from "vue";
import App from "./App.vue";
import "nprogress/nprogress.css";

import { createRouter, createWebHistory } from "vue-router";
import Home from "./components/Home.vue";
import Videos from "./components/Videos.vue";
import Gif from "./components/Gif.vue";
import Status from "./components/Status.vue";


const router = createRouter({

  history: createWebHistory(),

  routes: [
    {path: "/", redirect: "/home" },
    {path : "/home", component: Home},
    {path : "/video", component: Videos},
    {path : "/gif", component: Gif},
    {path : "/status", component: Status},

  ],

});


const app = createApp(App);
app.use(router);
app.mount("#app");
export { app };



