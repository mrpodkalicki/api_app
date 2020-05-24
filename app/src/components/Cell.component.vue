
<template>
    <div class="cell">
        {{TeamHome}}
        {{TeamAway}}
        {{Percentage}}
    </div>
</template>

<script>
    export default {
        name: "Cell",

        props: {
            TeamHome:String,
            TeamAway: String,
            Percentage:String,
        },
        
    }

    
   
</script>

<style lang="scss" scoped>
    .cell{
        background: linear-gradient(180deg, #DF90FE 0%, #C93DFF 100%), #DF8DFE;
        box-shadow: inset 0px 2px 2px rgba(0, 0, 0, 0.25);
        border-radius: 10px;
        width: 22rem;
        height: 12rem;
        margin: 2rem;

    }

</style>