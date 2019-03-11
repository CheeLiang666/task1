import React, {Component} from 'react';
import FormInput from './FormInput';
import Register from './Register';

class Login extends Component{
    constructor(props){
        super(props);
        this.state = {
            modal: false,
        };
        this.toggle = this.toggle.bind(this);
    }

    toggle(){
        this.setState({
            modal: !this.state.modal,
        })
    }

    render(){
        return(
            <div className="container">
                <Register modal={this.state.modal} toggle={this.toggle}/>
                <div className="d-flex justify-content-end h-100">
                    <div className="card">
                        <div className="card-header">
                            <h3>Sign In</h3>
                        </div>
                        <div className="card-body">
                            <form>
                                <FormInput icon="envelope" type="email" placeholder="email" name="email"/>
                                <FormInput icon="key" type="password" placeholder="password" name="password"/>
                                <div className="row align-items-center remember">
                                    <input type="checkbox" name="checkbox" />Remember Me
                                </div>
                                <div className="form-group">
                                    <input type="submit" value="Sign In" className="btn float-right login_btn" />
                                </div>
                            </form>
                        </div>
                        <div className="card-footer">
                            <div className="d-flex justify-content-center links">
                                Don't have an account?<a href="#" onClick={this.toggle}>Sign Up</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Login;