import {GET_PATIENTS, DELETE_PATIENT, USER_LOGGED_OUT} from '../actions/index';

const initialState = {
    patients: []
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_PATIENTS:
            return {
                ...state,
                patients: action.payload
            };
        case DELETE_PATIENT:
            return {
                ...state,
                patients: state.patients.filter(patient => patient.id !== action.payload)
            };
        case USER_LOGGED_OUT:
            return null;
        default:
            return initialState;
    }
}
