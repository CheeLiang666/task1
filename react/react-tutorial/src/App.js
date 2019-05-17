import React, { Component } from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import Login from './Component/SignInAndSignUp/SignIn/Login';
import Home from './Component/Home/home';
import ProtectedRoute from './Component/protected_route';
import {withAuthentication} from './Component/Session';

function App(props){
    return(
        <BrowserRouter>
            <div className="full-height">
                <Switch>
                    <Route exact path="/" render={() => <Login /> } />
                    <Route exact path="/home" component={Home} />
                    <Route path="*" component={() => <h1 style={{color: "#eee"}}>404 Not Found!</h1>} />
                </Switch>
            </div>
        </BrowserRouter>
    )
}

export default withAuthentication(App);