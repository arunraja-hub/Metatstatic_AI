import { toastr } from 'react-redux-toastr';
import axios from 'axios';

export const USER_LOGGED_IN = "USER_LOGGED_IN";
export const USER_LOGGED_OUT = "USER_LOGGED_OUT";
export const GET_PATIENTS = "GET_PATIENTS";
export const DELETE_PATIENT = "DELETE_PATIENT";
export const GET_PATHOLOGYIMAGES = "GET_PATHOLOGYIMAGES";
const LOAD_IMAGES = 'LOAD_IMAGES';
const SELECT_IMAGE = 'SELECT_IMAGE';

export const someAction = (props) => {
    return (dispatch, getState) => {
        //toastr.success('Success', 'You clicked this button');
    }
}

export const login = (props) => {
    return (dispatch, getState) => {
        dispatch({
            type: USER_LOGGED_IN,
            payload: { username: "Siva", token: "Some Token" }
        });
        //toastr.success('Success', 'You have successfully login');
    }
}

export const logout = (props) => {
    return (dispatch, getState) => {
        dispatch({
            type: USER_LOGGED_OUT,
            payload: null
        });
        toastr.success('Success', 'You clicked login');
    }
}

//GET PATIENTS
export const getPatients = (props) => (dispatch, getState) => {
        axios
            //.get("http://localhost:8000/api/patients/")
            .get("/api/patients/")
            .then(res => {
                console.log(res.data);
                dispatch({
                    type: GET_PATIENTS,
                    payload: res.data
                });
                // toastr.success('Success', 'Retrieved Patients Data');
            })
            .catch(err => toastr.error('Error', 'Failed to Retrieve Patients'));
};

//DELETE PATIENTS
export const deletePatient = (id) => {
    return (dispatch, getState) => {
        axios
            .delete("/api/patients/" + id + "/")
            .then(res => {
                dispatch({
                    type: DELETE_PATIENT,
                    payload: id
                });
                toastr.success('Success', 'Patient Deleted');
            })
            .catch(err => toastr.error('Error', 'Failed to Delete Patient'));
    };
};

//GET PATHOLOGYIMAGES
export const getPathologyImages = (props) => (dispatch, getState) => {
    axios
        .get("http://localhost:8000//api/pathologyScan/")
        //.get("/api/pathologyScan/")
        .then(res => {
            console.log(res.data);
            dispatch({
                type: GET_PATHOLOGYIMAGES,
                payload: res.data
            });
            // toastr.success('Success', 'Retrieved Patients Data');
        })
        .catch(err => toastr.error('Error', 'Failed to Retrieve Patients'));
};

export function selectImage(image) {
    return {
      type: SELECT_IMAGE,
      image
    }
  }
  
  export function loadImages() {
    return {
      type: LOAD_IMAGES
    }
  }
