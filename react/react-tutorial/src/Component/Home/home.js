import React, { Component } from 'react';
import NavigationBar from '../NavigationBar';
import {withAuthorization} from '../Session';

class Home extends Component{

    constructor(props){
        super(props);
        this.state = {
            user: {},
        };
    }

    componentDidMount(){
        this.props.firebase.user(this.props.authUser.uid)
        .on('value', snapshot => {
            this.setState({
                user: snapshot.val(),
            });
        });
    }

    componentWillUnmount(){
        this.props.firebase.user(this.props.authUser.uid).off();
    }

    render(){
        return(
            <div className="container-fluid home">
                {/* <NavigationBar /> */}
                {/* <h1 style={{color: "#FF0000"}}>{this.state.user.userName}</h1> */}
                <button className="btn button" onClick={this.props.firebase.doSignOut}>Sign out</button>
            </div>
        );
    }    
}

const condition = authUser => !!authUser;

export default withAuthorization(condition)(Home);