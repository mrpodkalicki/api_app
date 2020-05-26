<template>
  <footer class="footer">
    <div class="footer__white_box">
      <a href="https://www.betclic.pl/koszykowka-s4" target="_blank">
        <div class="footer__white_box__lvbet"></div>
      </a>
      <!-- footer__box__lvbet -->
      <a
        href="https://lvbet.pl/pl/zaklady-bukmacherskie/multiple--?leagues=43559,12396"
        target="_blank"
      >
        <div class="footer__white_box__betclic"></div>
      </a>
      <!-- do fora -->
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer"
};
</script>

<style lang="scss" scoped>
.footer {
  margin: 0;
  height: 20vh; // na vh
  display: flex;
  justify-content: center;
  align-items: flex-end;

  &__white_box {
    width: 48rem;
    height: 9rem;
    background: linear-gradient(180deg, #ffffff 0%, #ffffff 85.42%), #960051;
    box-shadow: inset -5px -5px 4px rgba(0, 0, 0, 0.25);
    border-radius: 0 0 55px 55px;
    transform: rotate(179.88deg);
    display: flex;
    &__betclic {
      width: 21rem;
      height: 7rem;
      // border: solid red;
      background-image: url("../assets/icons/teams/Betclic.png");
      background-repeat: no-repeat;
      background-size: contain;
      transform: rotate(179.88deg);
    }
    &__lvbet {
      width: 21rem;
      height: 7rem;
      // border: solid red;
      background-image: url("../assets/icons/teams/lvbet.png");
      background-repeat: no-repeat;
      background-size: contain;
      transform: rotate(179.88deg);
    }
  }
}
</style>
