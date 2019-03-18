import React, { Component } from 'react';
import NavigationBar from '../NavigationBar/AuthNavigationBar';
import {withAuthorization} from '../Session';

class Home extends Component{

    constructor(props){
        super(props);
        this.state = {
            authUser: {},
        };
    }

    componentDidMount(){
        this.props.firebase.user(this.props.authUser.uid)
        .on('value', snapshot => {
            this.setState({
                authUser: snapshot.val(),
            });
        });
    }

    componentWillUnmount(){
        this.props.firebase.user(this.props.authUser.uid).off();
    }

    render(){
        return(
            <div className="full-width-height-container home">
                <NavigationBar authUserName={this.state.authUser.userName}/>
                {/* <h1 style={{color: "#FF0000"}}>{this.state.user.userName}</h1> */}
                {/* <button className="btn button" onClick={this.props.firebase.doSignOut}>Sign out</button> */}
            </div>
        );
    }    
}

const condition = authUser => !!authUser;

export default withAuthorization(condition)(Home);