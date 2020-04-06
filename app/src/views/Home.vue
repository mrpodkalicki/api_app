

<template>
  <div class="home_view">

      <Bar/>
      <Score/>

  </div>
</template>

<script>
// @ is an alias to /src
// jak towrzysz widok to -> home.view.vue
// jak dodajesz komponent to -> bar.component.vue

    import Bar from "../components/Bar";
    import Score from "../components/Score";

    export default {
      name: "Home",
      components: {
          Score,
          Bar,


    },
  data() {
    return {
      message: 'siema adidfdsfgdsg',
      variable: '',
    }
  },
  methods: {
    testHandler(value) {
      this.variable = value;
    },
  },
};
</script>

<style  lang="scss" scoped>

    .home_view {
        background-image: url('../assets/img/background.jpg');
        background-repeat: no-repeat;
        background-size: 100%;
        width: 100%;
        height: 100vh;

    }
</style>