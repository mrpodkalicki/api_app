<template>
  <div class="score">
    <Bar class="score__bar" />

    <div class="score__square-container">
      <div class="score__center-square">
        <div class="score__center-square__dark-box" v-if="!matchDate"></div>
        <div class="score__header">
          <h3 class="score__header__text score__header__element">
            {{ creatDataToDisplayFromAllValueInputs() }}
          </h3>
          <img
            src="../assets/icons/home/cale.svg"
            class="score__header__icon score__header__element"
          />
        </div>
        <fulfilling-bouncing-circle-spinner
          class="score__spinner"
          :animation-duration="4000"
          :size="60"
          color="#c93dff"
          v-if="!matchDate"
        />
        <div class="score__container-cell">
          <Cell
            v-for="(value, index) in matchDate"
            :key="index"
            :TeamHome="value['HOME']"
            :TeamAway="value['AWAY']"
            :Percentage="value['WIN']"
          />
        </div>
      </div>
    </div>
    <Footer class="score__footer" />
  </div>
</template>

<script>
import Bar from "../components/Bar.component.vue";
import Cell from "../components/Cell.component.vue";
import Footer from "../components/Footer.component.vue";
import axios from "axios";
import Vue from "vue";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";

import { FulfillingBouncingCircleSpinner } from "epic-spinners";

Vue.use(ElementUI);

export default {
  name: "Score",
  components: {
    FulfillingBouncingCircleSpinner,
    Bar,
    Cell,
    Footer,
  },
  props: {
    allValueInputs: String,
  },

  data() {
    return {
      pickedDate: "",
      matchDate: null,
      loading: true,
      apiUrl: "http://127.0.0.1:5000/prediction/",
      parmForAPi: "",
    };
  },
  methods: {
    changeLoading() {
      this.loading = false;
    },
    reduceYearFromInputValueToAPi() {
      const firstPartParameter = this.allValueInputs.slice(0, 4);
      const secondPartParameter = this.allValueInputs.slice(6, 8);
      return firstPartParameter + secondPartParameter;
    },
    creatDataToDisplayFromAllValueInputs() {
      const firstPartDate = this.allValueInputs.slice(0, 2);
      const secondPartDate = this.allValueInputs.slice(2, 4);
      const thirdPartDate = this.allValueInputs.slice(4, 8);
      return firstPartDate + "-" + secondPartDate + "-" + thirdPartDate;
    },
  },
  beforeRouteEnter(to, from, next) {
    next();
  },
  created() {
    console.log(this.allValueInputs, "input");
    this.pickedDate = this.allValueInputs;

    axios
      .get(this.apiUrl + this.reduceYearFromInputValueToAPi())
      .then(
        (response) => (
          (this.matchDate = response.data["result"]), (this.loading = false)
        )
      );
  },
};
</script>
<style lang="scss" scoped>
.score {
  background-image: url("../assets/img/background.jpg");
  background-repeat: no-repeat;
  background-size: 100%;
  width: 100%;
  height: 100vh;
  font-family: "Raleway", sans-serif;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
  &__bar {
    position: absolute;
    top: 0;
    right: 0;
  }

  &__header {
    display: flex;
    justify-content: center;
    align-content: center;
    align-items: center;

    &__element {
      flex-grow: 1;
      margin: 1rem;
    }
    &__text {
      font-weight: bold;
      font-size: 2.5rem;
      font-family: "Raleway", sans-serif;
      font-style: italic;
      letter-spacing: 0.1em;
      color: white;
    }
    &__icon {
      width: 3rem;
      height: 3rem;
    }
  }
  &__square-container {
    display: flex;
    width: 80%;
    justify-content: center;
    align-content: center;
  }
  &__center-square {
    background: linear-gradient(180deg, #8702b6 0%, #33024a 85.42%), #960051;
    box-shadow: inset 0.5rem 0.5rem 0.4rem rgba(0, 0, 0, 0.25);
    border-radius: 5.5rem;
    width: 90rem;
    height: 48rem;
    display: flex;
    align-items: center;
    flex-direction: column;
    padding: 1rem;
    overflow: auto;
    color: white;
    position: relative;
    &__dark-box {
      top: 0;
      left: 0;
      border-radius: 5.5rem;
      position: absolute;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.75);
    }
  }

  &__spinner {
    align-self: center;
    justify-self: center;
    margin: auto auto 30vh auto;
  }

  &__container-cell {
    display: grid;
    width: 55vw;
    grid-template-columns: repeat(auto-fit, 25rem);
    grid-template-rows: auto;
    gap: 2rem;
    justify-items: center;
    justify-content: center;
  }

  &__footer {
    position: absolute;
    bottom: 0px;
  }
}
</style>
