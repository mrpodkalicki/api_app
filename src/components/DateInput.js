import React from "react";


import Grid from '@material-ui/core/Grid';
import DateFnsUtils from '@date-io/date-fns';
import {
    MuiPickersUtilsProvider,
    KeyboardDatePicker,
} from '@material-ui/pickers';

export default function DateInput(props) {
    // The first commit of Material-UI


    const handleDateChange = date => {
        props.setSelectedDate(date);
    };

    return (
        <div className = {"calendar"}>
            <MuiPickersUtilsProvider    utils={DateFnsUtils}>
                <KeyboardDatePicker
                    disableToolbar
                    variant="inline"
                    inputVariant = "outlined"
                    autoOk = {true}
                    disableFuture = {true}
                    format="dd/MM/yyyy"
                    margin="normal"
                    id="date-picker-inline"
                    label="Date"
                    value={props.value}
                    onChange={handleDateChange}
                    KeyboardButtonProps={{
                        'aria-label': 'change date',
                    }}
                />
            </MuiPickersUtilsProvider>
        </div>
    );
}

