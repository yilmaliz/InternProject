import axios from 'axios';

import {GET_TWEETS} from './types';

//GET TWEETS

export const getTweets = () => dispatch => {
    axios.get('/tweet')
    .then(res => {
        dispatch({

            type : GET_TWEETS,
            payload : res.data
        });
    })
    .catch(err = console.log(err));



};