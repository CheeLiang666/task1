import React, {Component} from 'react';
import FormInput from './FormInput';

class SignUp extends Component{
    constructor(props){
        super(props);
        this.handleCloseButtonEvent = this.handleCloseButtonEvent.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleCloseButtonEvent(e){
        document.getElementById("signup").style.display = 'none';
    }

    handleSubmit(e){
        //alert(e.target["userName"].value);
    }

    render(){
        return(
            <div id="signup" className="modal">
                <div className="signup-card animate">
                    <div className="card-header">
                        <span className="close" title="Close Modal" onClick={this.handleCloseButtonEvent}>x</span>
                        <h3>Sign Up</h3>
                    </div>
                    <div className="card-body">
                        <form onSubmit={this.handleSubmit}>
                            <FormInput icon="user" type="text" placeholder="username" name="userName"/>
                            <FormInput icon="envelope" type="email" placeholder="email" name="email"/>
                            <FormInput icon="key" type="password" placeholder="password" name="password" />
                            <FormInput icon="key" type="password" placeholder="confirm password" name="confirmPwd" />
                            <div className="form-group">
                                <input type="submit" value="Sign Up" className="btn signup-button" />
                                <a href="#" className="float-right">Forgot password?</a>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}

export default SignUp;