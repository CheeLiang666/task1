import React, { Component } from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import Login from './Component/Login';
import Home from './Component/home';
import ProtectedRoute from './Component/protected_route';
class App extends Component{
    render(){
        return(
            <BrowserRouter>
                <div className="full-height">
                    <Switch>
                        <Route exact path="/" component={Login} />
                        <ProtectedRoute exact path="/home" component={Home} />
                        <Route path="*" component={() => <h1 style={{color: "#eee"}}>404 Not Found!</h1>} />
                    </Switch>
                </div>
            </BrowserRouter>
        )
    }
}

export default App;