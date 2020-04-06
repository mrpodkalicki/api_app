<template>
    <div class="bar">  <!-- class="bar" -->
        <ul class = "bar__list"> <!-- class="bar__list" -->
            <li class="bar__list__element"> <!-- class="bar__list__element" -->
                PREDYKATOR
            </li>

            <li class="bar__list__element">
                INFORMACJE
            </li>

            <li class="bar__list__element">
                KOSZYKÓWKA
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Bar",
        data() {
            return {
                menu: ["PREDYKATOR","INFORMACJE","KOSZYKÓWKA"],
            }
        }
    }
</script>

<style  lang="scss" scoped>
    .bar{
        font-size: 10px;
        width: 100%;
        display: flex;
        justify-content: flex-end;
        text-align: center;
        &__list{
            width: 83.9rem;
            list-style-type:none;
            display: flex;
            flex-direction: row;
            margin: 1.5rem 0 0 0 ;
            padding: 1.5rem;
            &__element{
                font-size:3rem;
                color: white;
                flex-grow: 1;
                font-family: 'Raleway', sans-serif;
                font-style: normal;
                font-weight: 700;
                letter-spacing: 0.1em;
            }
        }
    }

</style>