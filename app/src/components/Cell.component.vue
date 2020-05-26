<template>
  <div class="cell">
    <div class="cell__grid-container">
      <div class="cell__grid-element">
        <img
          class="cell__team-icon"
          :src="getImgUrl(TeamHome)"
          alt="team icon"
        />
      </div>
      <div class="cell__grid-element">
        <img
          class="cell__team-icon"
          :src="getImgUrl(TeamAway)"
          alt="team icon"
        />
      </div>
      <div class="cell__grid-element">{{ Percentage }}</div>
      <div class="cell__grid-element">{{ calculationScoreForLoserTeam() }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Cell",

  props: {
    TeamHome: String,
    TeamAway: String,
    Percentage: String,
  },
  methods: {
    getImgUrl(imgName) {
      return require("../assets/icons/teams/" + imgName + ".png");
    },
    calculationScoreForLoserTeam() {
      const percent = this.Percentage.slice(0, 5);
      const percentageLoseTeam = 100 - +percent;
      const aroundNumbeToTwoDecimal = percentageLoseTeam.toFixed(2);
      return aroundNumbeToTwoDecimal + "%";
    },
  },
};
</script>

<style lang="scss" scoped>
.cell {
  background: linear-gradient(180deg, #df90fe 0%, #c93dff 100%), #df8dfe;
  box-shadow: inset 0px 2px 2px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
  width: 22rem;
  height: 13rem;
  margin: 2rem;
  padding: 0.5rem;

  &__grid-container {
    margin: 2px auto;
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: 48% 48%;
    grid-row: auto auto;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
  }

  &__grid-element {
    padding: 2px;
    border-radius: 1px;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: sans-serif;
    text-shadow: 0px 2px 2px rgba(0, 0, 0, 0.25);
    font-family: "Roboto", sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 2rem;
  }

  &__team-icon {
    width: 8rem;
    height: 8rem;
    filter: drop-shadow(0px 2px 2px rgba(0, 0, 0, 0.25));
  }
}
</style>
