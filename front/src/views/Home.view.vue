<template>
  <div class="home-view">
    <Bar class="home-view__bar" />
    <div class="home-view__center-square-container">
      <div class="home-view__center-square">
        <div class="center-square__header-container center-square__child">
          <div class="center-square__header">
            <h3 class="center-square__header__text">WYBIERZ DATE</h3>
            <div class="center-square__header__icon"></div>
          </div>
        </div>
        <div class="center-square__input-container center-square__child">
          <div class="center-square__oval-input-wraper">
            <input
              v-for="(item, index) in dateTypes"
              :key="index"
              :class="
                `center-square__input center-square__input__${item.class}`
              "
              :placeholder="`${item.label}`"
              v-model="item.inputValue"
            />
          </div>
        </div>
        <div class="center-square__btn-container center-square__child">
          <router-link
            :to="{
              name: 'Score',
              params: {
                allValueInputs:
                  dateTypes[0].inputValue +
                  dateTypes[1].inputValue +
                  dateTypes[2].inputValue,
              },
            }"
          >
            <button to="/score" class="center-square__btn center-square__item">
              <a class="center-square__btn__link" href="#"></a>
              <div class="center-square__btn__text-wraper">
                <span>POKAZ</span>
                <span>MECZE</span>
              </div>
            </button>
          </router-link>
        </div>
      </div>
    </div>
    <Footer class="home-view__footer" />
  </div>
</template>

<script>
import Bar from "../components/Bar.component.vue";
import Footer from "../components/Footer.component.vue";

export default {
  name: "Home",
  components: {
    Bar,
    Footer,
  },
  data() {
    return {
      dateTypes: [
        {
          label: "MM",
          class: "month",
          inputValue: "",
        },
        {
          label: "DD",
          class: "day",
          inputValue: "",
        },
        {
          label: "YYYY",
          class: "year",
          inputValue: "",
        },
      ],
      pickedDate: "10-10-2020",
      apiMatchDate: null,
      allValueInputs: this.dateTypes,
    };
  },

  methods: {},
};
</script>

<style lang="scss" scoped>
.home-view {
  background-image: url("../assets/img/background.jpg");
  background-repeat: no-repeat;
  background-size: 100%;
  width: 100%;
  height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  overflow: hidden;
  &__bar {
    position: absolute;
    top: 0;
    right: 0;
  }
  &__center-square-container {
    height: 70vh; // inny niz %
    display: flex;
    justify-content: center;
    align-items: center;
  }
  &__center-square {
    margin: 20rem 0 0 0;
    width: 48rem;
    height: 44rem;
    left: 50rem;
    top: 25rem;
    background: linear-gradient(180deg, #8702b6 0%, #33024a 85.42%), #960051;
    box-shadow: inset 0.5rem 0.5rem 0.4rem rgba(0, 0, 0, 0.25);
    border-radius: 5.5rem;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
  &__footer {
    position: absolute;
    bottom: 0px;
  }
}

.center-square {
  &__child {
    flex-grow: 1;
  }
  &__header {
    display: flex;
    justify-content: center;
    align-items: center;
    &__text {
      color: white;
      font-family: "Raleway", sans-serif;
      font-style: italic;
      font-weight: 700;
      font-size: 25px;
      line-height: 3rem;
      text-align: center;
      letter-spacing: 0.1rem;
    }
    &__icon {
      width: 3.5rem;
      height: 3.5rem;
      background-image: url("../assets/icons/home/cale.svg");
      background-size: contain;
      margin: 0 1rem;
    }
  }
  &__oval-input-wraper {
    width: 39rem;
    height: 11.5rem;
    background: linear-gradient(180deg, #9c00d2 0%, #56007e 100%), #960051;
    box-shadow: inset 0.5rem 0.5rem 0.4rem rgba(0, 0, 0, 0.25);
    border-radius: 55px;
    display: flex;
    flex-direction: row;
    max-width: 100%;
    justify-content: center;
    align-items: center;
  }

  &__input {
    background: linear-gradient(180deg, #df90fe 0%, #c93dff 100%), #df8dfe;
    box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 2.5rem;
    height: 5.6rem;
    max-width: 7rem;
    flex-grow: 1;
    margin: 1rem;
    text-align: center;
    font-family: "Roboto", sans-serif;
    font-size: 2.4rem;
    line-height: 2.8rem;
    letter-spacing: 0.1rem;
    border: none;
    color: rgba(255, 255, 255, 0.81);
    font-weight: 900;
    text-shadow: inset 1px 2px 2px rgba(0, 0, 0, 0.25);
    outline: none;

    &__year {
      min-width: 10.5rem;
    }
  }

  &__input::placeholder {
    color: rgba(255, 255, 255, 0.51);
    font-weight: 900;
    font-family: "Roboto", sans-serif;
    font-size: 2.4rem;
    line-height: 2.8rem;
    letter-spacing: 0.1rem;
    text-shadow: inset 0.1rem 0.2rem 0.2rem rgba(0, 0, 0, 0.25);
  }

  &__btn {
    width: 242px;
    color: white;
    font-size: 2.4rem;
    font-family: "Roboto", sans-serif;
    font-style: normal;
    font-weight: 700;
    height: 6.5rem;
    background: linear-gradient(180deg, #009b76 0%, #014b46 100%), #06bc7a;
    box-shadow: 0.2rem 0.2rem 0.2rem rgba(0, 0, 0, 0.25);
    border-radius: 5.5rem;
    border: 0.1px;
    position: relative;

    &__link {
      position: absolute;
      width: 100%;
      height: 100%;
      top: 0px;
      left: 0px;
    }

    &__text-wraper {
      display: flex;
      flex-direction: column;
      padding: 0.5rem;
      letter-spacing: 0.2rem;
    }
  }
}
</style>
