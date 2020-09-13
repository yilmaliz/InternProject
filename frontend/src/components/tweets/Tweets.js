import React, { Component, Fragment } from 'react';

import {connect} from 'react-redux';
import PropTypes from 'prop-types';

import {getTweets} from '../../actions/tweets';


export class Tweets extends Component{
    static propTypes = {
        tweets: PropTypes.array.isRequired
    };

    componentDidMount() {
        this.props.getTweets();
    }

    render() {

        return (
            <Fragment>
                <h2>Tweet</h2>
                <table className= "table table-striped">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>CONTENT</th>
                            <th>OWNER</th>
                            <th>COMMENTS NUMBER</th>
                            <th>LIKES NUMBER</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.tweets.map( tweet =>(
                            <tr key={tweet.is}>
                                <td>{tweet.id}</td>
                                <td>{tweet.content}</td>
                                <td>{tweet.owner}</td>
                                <td>{tweet.number_of_comments}</td>
                                <td>{tweet.number_of_likes}</td>
                            </tr>

                        ))}
                    </tbody>
                </table>

            </Fragment>
        );
    };

}
const mapStateToProps = state => ({
    tweets:state.tweets.tweets
});
export default connect(mapStateToProps, {getTweets})(Tweets);