<template>
  <div class="score">
    <Bar />
    <div class="score__square-container">
      <div v-if="!matchDate">loading</div>
      <div v-if="matchDate" class="score__center-square">
        <div class="score__header">
          <h3 class="score__header__text score__header__element">{{pickedDate}}</h3>
          <img
            src="../assets/icons/home/KALENDARZ.png"
            class="score__header__icon score__header__element"
          />
        </div>
        <div class="score__container-cell">
          <Cell
            v-for="(value, index) in matchDate"
            :key="index"
            :TeamHome="value['HOME']"
            :TeamAway="value['AWAY']"
            :Percentage="value['WIN']"
          />
          <!-- {{matchDate}} -->
        </div>
        <!-- {{matchDate}} -->
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Bar from "../components/Bar.component.vue";
import Cell from "../components/Cell.component.vue";
import Footer from "../components/Footer.component.vue";
import axios from "axios";

export default {
  name: "Score",
  components: {
    Bar,
    Cell,
    Footer
  },
  props: {
    //  TeamOne:String
  },

  data() {
    return {
      pickedDate: "10-10-2020",
      matchDate: null
    };
  },
  beforeRouteEnter(to, from, next) {
    next();
    console.log(from, "from");
  },
  created() {
    //    this.matchDate = this.$route.params.apiDate;
    axios
      .get("http://127.0.0.1:5000/prediction/112119")
      .then(
        response => (
          (this.matchDate = response.data["result"]),
          console.log(response, "resr")
        )
      );
    //    console.log(this.$route.params.apiDate)
  }
};
</script>

<style lang="scss" scoped>
.score {
  // border: solid red 5px;
  background-image: url("../assets/img/background.jpg");
  background-repeat: no-repeat;
  background-size: 100%;
  width: 100%;
  height: 100vh;
  overflow: auto;
  font-family: "Raleway", sans-serif;
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
    justify-content: center;
    align-content: center;
  }
  &__center-square {
    background: linear-gradient(180deg, #8702b6 0%, #33024a 85.42%), #960051;
    box-shadow: inset 0.5rem 0.5rem 0.4rem rgba(0, 0, 0, 0.25);
    border-radius: 5.5rem;
    width: 124rem;
    height: 60rem;
    display: flex;
    align-items: center;
    flex-direction: column;
    padding: 1rem;
    overflow: auto;
    // padding: 2rem;
  }

  &__container-cell {
    display: grid;
    width: 60vw;
    grid-template-columns: repeat(auto-fit, 25rem);
    gap: 2rem;
    justify-items: center;
    justify-content: center;
  }
}
</style>