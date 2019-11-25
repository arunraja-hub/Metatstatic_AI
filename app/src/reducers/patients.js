import { GET_PATIENTS} from "../actions/type.js";
import { functionTypeAnnotation } from "@babel/types";

const initialState = {
    patients : []
}

export default function(state = initialState, action){
    switch(action.type){
        case GET_PATIENTS:
            return{
                ...state,
                patients : action.payload
            }
        default:
            return state;
    }
}