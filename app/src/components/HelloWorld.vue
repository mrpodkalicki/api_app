<template>
  <div class="container">
    <!-- <input :value="userInput" @input="onInputChange($event.target.value)"/> -->
<!--    <input v-model="userInput" @keydown.enter="saveValue()">-->
<!--    our input value: {{ userInput }}-->

<!--    <div class="container__list">-->
<!--      Prop: {{ message }}-->
<!--      {{test}}-->
     <div class="container__list-item" v-for="(item, index) in list" :key="index">-->
       <span :class="`container__list-item&#45;&#45;${item}`">
      
       {{ item }}</span>
  </div>
<!--    </div>-->
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    message: String,
  },
  data() {
    return {
      userInput: '',
      list: [],
      test: this.$store.state.storeVariable,
    }
  },
  computed: {
    // getStyles() {
    //   return (item)=>{
    //     return {
    //       'container__list-item--green': item === 'aaaa',
    //       'container__list-item--red': item.length > 5,
    //       'container__list-item--yellow': item.length === 1,
    //     }
    //   }
    // },
    myNumber() {
      return `Moja cyfra to: ${this.number}`
  },

  getStoreValue() {
    return `get value from store: ${this.$store.state.storeVariable}`
  }
  },
  methods: {
    clickHandler() {
      this.number+=1;
    },
    onInputChange(value) {
      this.userInput = value;
    },
    saveValue() {
      const messageFromComponent = "ide z komponentu"

      this.list.push(this.userInput);
      this.userInput = '';

      this.$emit('onInputEnter', messageFromComponent);
    }
  },
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss"
        scoped>


.container {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;

  &__list-item {
    color: blue;
 
    &--red {
      color: red;
    }

    &--green {
      color: green;
    }

    &--yellow {
      color: yellow;
    }
  }
}

</style>
