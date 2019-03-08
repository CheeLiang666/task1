import React, {Component} from 'react';
import NavigationBar from './NavigationBar';

class Login extends Component{
    render(){
        return(
            <div className='container-fluid'>
                <NavigationBar activeStatus='active'/>
                <h1>Hello, world!</h1>
            </div>
        );
    }
}

export default Login;