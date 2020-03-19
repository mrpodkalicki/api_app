import React from "react";
import './Home.css'
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';
import DateInput from "../components/DateInput";
import axios from 'axios'

const submit = (dataDate, APIlink) =>{
    axios.get(`${APIlink}`)
    console.log(dataDate,APIlink)
}



const useStyles = makeStyles(theme => ({
    root: {
        '& > *': {
            margin: theme.spacing(1),
            width: '100%',
        },
    },
}));

const Home =  () => {
    const classes = useStyles();
    const [selectedDate, setSelectedDate] = React.useState(new Date());
    const [inputDate, setInputDate] = React.useState('');
    const prepareDate = `${selectedDate.getFullYear()}${selectedDate.getMonth() +1}${selectedDate.getDate()}`


    return (
        <div className={"container"}>
            <form className={"container__form"}>
                <div className={"container__form__input"}>
                    <TextField  onChange={e =>setInputDate(e.target.value)} value={inputDate} className={classes.root} id="outlined-basic" label="API" variant="outlined" />
                </div>
                <DateInput setSelectedDate = {setSelectedDate} value = {selectedDate} />
                <div className={"container__form__btn"}>
                    <Button   onClick={() => submit(prepareDate, inputDate)} variant="contained" color="primary">
                        SUBMIT
                    </Button>
                </div>

            </form>

        </div>
    )
}

export default  Home;
