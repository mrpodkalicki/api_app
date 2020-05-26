import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.view.vue";
import Score from "../views/Score.view.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    props: true,
  },
  {
    path: "/score",
    name: "Score",
    component: Score,
    props: true,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
