import React from "react";
import './Home.css'
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';
import DateInput from "../components/DateInput";
import Score from "../components/Score";
import axios from 'axios'



const submit = async (dataDate, APIlink, setError, setScore) =>{
    const allValue = {dateValue:dataDate, apiValue:APIlink}
    const errorValue = validationForm(allValue);
    setError(errorValue)
    if (!errorValue.apiInputError & !errorValue.dateInputError  ){
        console.log(dataDate)
        await axios.get(`${APIlink}`)
            .then(
                resp => {console.log(resp.data)
                    const source = resp.data;
                    setScore(source)
                }
            )
            .catch(err => console.log(err))

    }

}

const validationForm = (valueInput)  =>{
    let error = { }
        error = !(valueInput.apiValue) ? {...error,apiInputError: true}: {...error,apiInputError: false};
        error = !(valueInput.dateValue) ? {...error,dateInputError: true}: {...error,dateInputError: false};
    return error;
}

const useStyles = makeStyles(theme => ({
    root: {
        '& > *': {
            margin: theme.spacing(1),
            width: '100%',
        },
    },
}));

const prepareDateFromCalendar = (date) => {
    const day = date.getDate() < 10 ? `${0}${date.getDate()}`: date.getDate() ;
    const month = date.getMonth() +1 < 10 ? `${0}${date.getMonth() +1}`: date.getMonth() +1 ;
    const year = ''+ date.getFullYear()
    console.log(year[3])
    return `${month}${day}${year[2]}${year[3]}`
}

const Home =  () => {
    const classes = useStyles();
    const [selectedDate, setSelectedDate] = React.useState(new Date());
    const [inputDate, setInputDate] = React.useState('http://localhost:3002/result');
    const [errorInput, setError] =  React.useState({dateInputError:false, apiInputError:false});
    const [score, setScore] =  React.useState([]);
    const prepareDate = prepareDateFromCalendar(selectedDate);

    return (
        <div className={"container"}>
            <div className={"container__container_form"}>
                <form className={"container__form"}>
                    <div className={"container__form__input"}>
                        <TextField
                            error ={errorInput.apiInputError}
                            onChange={e =>setInputDate(e.target.value)}
                            value={inputDate} className={classes.root}
                            id="outlined-basic" label="API"
                            variant="outlined" />
                        <div>{errorInput.apiInputError ? "requiere" : ""}</div>

                    </div>
                    <DateInput
                        error ={errorInput.dateInputError}
                        setSelectedDate = {setSelectedDate}
                        value = {selectedDate}
                    />
                    <div className={"container__form__btn"}>
                        <Button   onClick={() => submit(prepareDate, inputDate, setError , setScore)} variant="contained" color="primary">
                            SUBMIT
                        </Button>
                    </div>
                </form>
            </div>
            <div className={"container__score"}>
                <Score score = {score}/>
            </div>

        </div>
    )
}

export default  Home;
