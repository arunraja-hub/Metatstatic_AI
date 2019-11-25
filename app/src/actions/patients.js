import axios from 'axios';

//GET PATIENTS
export const getPatients = () => dispatch =>{
    axios.get('/api/patients')
        .then(res => {
            dispatch({
                type: GET_PATIENTS,
                payload: res.data
            });
        }).catch(err => console.log(err));
}