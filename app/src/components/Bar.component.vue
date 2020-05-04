<template>
  <div class="bar">
    <!-- class="bar" -->
    <ul class="bar__list">
      <!-- class="bar__list" -->
      <div class="bar__list__container_element" v-for="(item, index) in navBarDate" :key="index">
        <router-link :to = "`${item.root}`">
          <li class="bar__list__element">{{item["text"]}}</li>
          <div :class="`bar__list__icon  ${item.className}`"></div>
          <a class="bar__list__link" href="#"></a>
        </router-link>
      </div>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Bar",
  data() {
    return {
      navBarDate:[
        {
          text:"PREDYKTOR",
          className:"bar__list__predict_icon",
          root: "/"
        },
        {
          text:"INFORMACJE",
          className:"bar__list__info_icon",
          root:"/"
        },
        {
          text:"KOSZYKÓWKA",
          className:"bar__list__football_icon",
          root:"/"
        }

      ],

      menuText: ["PREDYKTOR", "INFORMACJE", "KOSZYKÓWKA"],
      iconClass: [
        "bar__list__predict_icon",
        "bar__list__info_icon",
        "bar__list__football_icon"
      ]
    };
  }
};
</script>

<style  lang="scss" scoped>
.bar {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  text-align: center;
  height: 10vh;

  &__list {
    // border: solid red;
    width: 50%;
    list-style-type: none;
    display: flex;
    flex-direction: row;
    margin: 1.5rem 3rem 0 0;
    padding: 1.5rem;

    &__container_element {
      font-size: 3rem;
      color: white;
      flex-grow: 1;
      font-family: "Raleway", sans-serif;
      font-style: normal;
      font-weight: 700;
      letter-spacing: 0.1em;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      position: relative;
    }

    &__icon {
      width: 3rem;
      height: 3rem;
      // border: solid red;
      background-image: url("../assets/icons/home/INFORMACJE.png");
      background-size: contain;
      margin: 0 1rem;
    }

    &__link {
      position: absolute;
      width: 100%;
      height: 100%;
    }

    &__predict_icon {
      background-image: url("../assets/icons/home/PREDYKTOR.png");
    }

    &__info_icon {
      background-image: url("../assets/icons/home/INFORMACJE.png");
    }

    &__football_icon {
      background-image: url("../assets/icons/home/KOSZYKÓWKA.png");
    }
  }
}
</style>