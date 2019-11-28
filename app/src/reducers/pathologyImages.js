import {GET_PATHOLOGYIMAGES, USER_LOGGED_OUT} from '../actions/index';

const initialState = {
    pathologyImages: []
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_PATHOLOGYIMAGES:
            return {
                ...state,
                pathologyImages: action.payload
            };
        case USER_LOGGED_OUT:
            return null;
        default:
            return initialState;
    }
}