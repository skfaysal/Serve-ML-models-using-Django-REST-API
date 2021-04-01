
import React from 'react'
import axios from 'axios';
import * as settings from '../settings';

import CssBaseline from '@material-ui/core/CssBaseline';
import { withStyles, makeStyles } from '@material-ui/core/styles';
import { Container, Grid, Paper, Typography, Slider, Button } from '@material-ui/core';

// ########################################################
// Material UI inline styles
// ########################################################
const useStyles = makeStyles((theme) => ({
    container: {
        maxWidth: "75%",
        marginTop: "15vh",
        marginBottom: "10vh",
        borderRadius: '6px',
        backgroundColor: theme.palette.action.disabledBackground,
    },
    title: {
        marginTop: theme.spacing(2),
        marginBottom: theme.spacing(2),
        padding: theme.spacing(2), paddingLeft: theme.spacing(4),
        color: theme.palette.primary.main,
    },
    sliders: {
        paddingTop: theme.spacing(1),
        paddingBottom: theme.spacing(1),
        paddingLeft: theme.spacing(4),
        paddingRight: theme.spacing(4),
        marginBottom: theme.spacing(2),
    },
    slidertop: {
        marginTop: theme.spacing(2),
    }
}));

// ########################################################
// Our Custom IRIS slider. You may use the default slider instead of this
// ########################################################
const IrisSlider = withStyles({
    root: {
        color: '#751E66',
    },
    valueLabel: {
        left: 'calc(-50% -2)',
        top: -22,
        '& *': {
            background: 'transparent',
            color: '#000',
        },
    },
    mark: {
        height: 8,
        width: 1,
        marginTop: -3,
    },
    markActive: {
        opacity: 1,
        backgroundColor: 'currentColor',
    },
})(Slider);

// Marks on the slider track
const marks = [{ value: 0 }, { value: 100}];

// ########################################################
// The main Home component returned by this Module
// ########################################################
function Home(props) {
    // Material UI Classes 
    const classes = useStyles();

    // React hook state variable - Dimensions
    const [dimensions, setDimensions] = React.useState({
        "Pregnancies":5,
        "Glucose":50,
        "BloodPressure":50,
        "SkinThickness":50,
        "Insulin":50,
        "BMI":50,
        "DiabetesPedigreeFunction":50,
        "Age":50
    });
    // React hook state variable - Prediction
    const [prediction, setPrediction] = React.useState(null)

    // Function to update the Dimensions state upon slider value change
    const handleSliderChange = name => (event, newValue) => {
        setDimensions(
            {
                ...dimensions,
                ...{ [name]: newValue }
            }
        );
    };

    // Function to make the predict API call and update the state variable - Prediction 
    const handlePredict = event => {
        // Submit Iris Flower measured dimensions as form data
        let irisFormData = new FormData();
        irisFormData.append("Pregnancies", dimensions.Pregnancies);
        irisFormData.append("Glucose", dimensions.Glucose);
        irisFormData.append("BloodPressure", dimensions.BloodPressure);
        irisFormData.append("SkinThickness", dimensions.SkinThickness);

        irisFormData.append("Insulin", dimensions.Insulin);
        irisFormData.append("BMI", dimensions.BMI);
        irisFormData.append("DiabetesPedigreeFunction", dimensions.DiabetesPedigreeFunction);
        irisFormData.append("Age", dimensions.Age);

        //Axios variables required to call the predict API
        let headers = { 'Authorization': `Token ${props.token}` };
        let url = settings.API_SERVER + '/api/predict/';
        let method = 'post';
        let config = { headers, method, url, data: irisFormData };

        //Axios predict API call
        axios(config).then(
            res => {setPrediction(res.data["Prediced Diabetes status"])
            }).catch(
                error => {alert(error)})

    }

    function valuetext(value) {
        return `${value} cm`;
    }

    return (
        <React.Fragment>
            <CssBaseline />
            <Container fixed className={classes.container}>
                <Grid container alignItems="center" spacing={3}>
                    <Grid item xs={6}>
                        <Paper className={classes.title} elevation={0}>
                            <Typography variant="h5">
                                Diabetes Prediction
                            </Typography>
                        </Paper>
                        <Paper className={classes.sliders}>
                            <Typography id="Pregnancies" variant="caption" >
                                Pregnancies
                            </Typography>
                            <IrisSlider
                                defaultValue={3}
                                getAriaValueText={valuetext}
                                aria-labelledby="Pregnancies"
                                step={1}
                                min={0}
                                max={20}
                                valueLabelDisplay="on"
                                marks={marks}
                                className={classes.slidertop}
                                onChange={handleSliderChange("Pregnancies")}
                            />
                            <Typography id="Glucose" variant="caption" gutterBottom>
                                Glucose
                            </Typography>
                            <IrisSlider
                                defaultValue={20}
                                getAriaValueText={valuetext}
                                aria-labelledby="Glucose"
                                step={5}
                                min={0}
                                max={200}
                                valueLabelDisplay="on"
                                marks={marks}
                                className={classes.slidertop}
                                onChange={handleSliderChange("Glucose")}
                            />
                            <Typography id="BloodPressure" variant="caption" gutterBottom>
                                BloodPressure
                            </Typography>
                            <IrisSlider
                                defaultValue={60}
                                getAriaValueText={valuetext}
                                aria-labelledby="BloodPressure"
                                step={5}
                                min={0}
                                max={200}
                                valueLabelDisplay="on"
                                marks={marks}
                                className={classes.slidertop}
                                onChange={handleSliderChange("BloodPressure")}
                            />
                            <Typography id="SkinThickness" variant="caption" gutterBottom>
                                SkinThickness
                            </Typography>
                            <IrisSlider
                                defaultValue={10}
                                getAriaValueText={valuetext}
                                aria-labelledby="SkinThickness"
                                step={5}
                                min={0}
                                max={100}
                                valueLabelDisplay="on"
                                marks={marks}
                                className={classes.slidertop}
                                onChange={handleSliderChange("SkinThickness")}
                            />
                            <Typography id="Insulin" variant="caption" gutterBottom>
                                Insulin
                            </Typography>
                            <IrisSlider
                                defaultValue={10}
                                getAriaValueText={valuetext}
                                aria-labelledby="Insulin"
                                step={5}
                                min={0}
                                max={150}
                                valueLabelDisplay="on"
                                marks={marks}
                                className={classes.slidertop}
                                onChange={handleSliderChange("Insulin")}
                            />
                            <Typography id="BMI" variant="caption" gutterBottom>
                                BMI
                            </Typography>
                            <IrisSlider
                                defaultValue={30}
                                getAriaValueText={valuetext}
                                aria-labelledby="BMI"
                                step={2}
                                min={0}
                                max={150}
                                valueLabelDisplay="on"
                                marks={marks}
                                className={classes.slidertop}
                                onChange={handleSliderChange("BMI")}
                            />
                            <Typography id="DiabetesPedigreeFunction" variant="caption" gutterBottom>
                                DiabetesPedigreeFunction
                            </Typography>
                            <IrisSlider
                                defaultValue={0.2}
                                getAriaValueText={valuetext}
                                aria-labelledby="DiabetesPedigreeFunction"
                                step={0.1}
                                min={0}
                                max={10}
                                valueLabelDisplay="on"
                                marks={marks}
                                className={classes.slidertop}
                                onChange={handleSliderChange("DiabetesPedigreeFunction")}
                            />
                            <Typography id="Age" variant="caption" gutterBottom>
                                Age
                            </Typography>
                            <IrisSlider
                                defaultValue={20}
                                getAriaValueText={valuetext}
                                aria-labelledby="Age"
                                step={1}
                                min={0}
                                max={100}
                                valueLabelDisplay="on"
                                marks={marks}
                                className={classes.slidertop}
                                onChange={handleSliderChange("Age")}
                            />
                        </Paper>
                    </Grid>
                    <Grid item xs={2}>
                        <Button variant="contained" color="primary" onClick={handlePredict}>
                            Predict
                        </Button>
                    </Grid>
                    <Grid item xs={4}>
                        <Paper className={classes.title} elevation={0}>
                            <Typography variant="caption" display="inline">
                                Predicted Diabetes: <span>&nbsp;</span>
                            </Typography>
                            <Typography variant="body1" display="inline">
                                {prediction}
                            </Typography>
                        </Paper>
                    </Grid>
                </Grid>
            </Container>
        </React.Fragment>
    )
}

export default Home
