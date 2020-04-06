<template>
    <div class="score">
        <div  class="score__box" >
            <p class="score__box__text">03-02-2020</p>
            <div class=""></div>
            <div class="score__box__container-cell">

                <Cell    v-for = " n in 3" :key="n "/>
            </div>
            <Button class="score__box__btn">POKAŻ PREDYKCJE</Button>
        </div>
    </div>
</template>

<script>
    import Cell from "./Cell";
    export default {
        name: "Score",
        components: {
            Cell
        }
    }
</script>

<style lang="scss" scoped>
    .score{
        margin: 5rem 0 0 0;
        display: flex;
        justify-content: center;
        padding: 1rem;
        font-family: 'Raleway', sans-serif;

        &__box{
            background: linear-gradient(180deg, #8702B6 0%, #33024A 85.42%), #960051;
            box-shadow: inset .5rem .5rem .4rem rgba(0, 0, 0, 0.25);
            border-radius: 5.5rem;
            width: 124rem;
            height: 61rem;
            display: flex;
            align-items: center;
            flex-direction: column;
            padding: 1rem;


            &__text{
                color: white;
                font-style: italic;
                font-weight: 700;
                font-size: 2.5rem;
                text-align: center;
                letter-spacing: 0.1rem;

            }
            &__container-cell{

                width: 100%;
                height: 70%;


            }

            &__btn{
                background: linear-gradient(180deg, #009B76 0%, #014B46 100%), #06BC7A;
                box-shadow: 2px 2px 3px rgba(0, 0, 0, 0.25);
                border-radius: 5.5rem;
                width: 24.2rem;
                height: 6.7rem;
                font-style: normal;
                font-weight: 700;
                font-size: 24px;
                line-height: 28px;
                text-align: center;
                letter-spacing: 0.1rem;
                color: white;
                margin: 2rem ;
            }
        }
    }

</style>