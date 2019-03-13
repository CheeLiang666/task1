import React, {Component} from 'react';
import FormInput from './FormInput';
import InvalidMsg from './InvalidMsg';
import ModalComponent from './ModelComponent';
import { Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';


class Register extends Component{
    constructor(props){
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.state = {
            passwordStatus: true,
            invalidMsg: null,
            emailStatus: true,
        };
        this.verifyPassword = this.verifyPassword.bind(this);
        this.verifyEmailAddress = this.verifyEmailAddress.bind(this);
        this.clearFormMsg = this.clearFormMsg.bind(this);
    }

    verifyEmailAddress(email){
        const accountsList = this.props.accountsList;
        for(let i = 0; i < accountsList.length; i++){
            if(email === accountsList[i].email){
                this.setState({
                    emailStatus: false,
                    invalidMsg: "Email had already been registered.",
                });
                return false;
            }else{
                continue;
            }
        }
        this.setState({
            emailStatus: true,
            invalidMsg: null,
            passwordStatus: true,
        });
        return true;
    }

    verifyPassword(password, confirmPwd){
        if(password.length < 4){
            this.setState({
                passwordStatus: false,
                invalidMsg: "Password length must be greater than or equal to 4.",
            });
            return false;
        }else{
            if(password === confirmPwd){
                //success
                this.setState({
                    passwordStatus: true,
                    invalidMsg: null,
                });
                return true;
            }else{
                this.setState({
                    passwordStatus: false,
                    invalidMsg: "Password and confirm password not matched.",
                });
                return false;
            }
        }
    }

    clearFormMsg(){
        this.setState({
            emailStatus: true,
            passwordStatus: true,
            invalidMsg: null,
        });
    }

    handleSubmit(e){
        e.preventDefault();
        const userName = e.target["userName"].value;
        const email = e.target["email"].value;
        const password = e.target["password"].value;
        const confirmPwd = e.target["confirmPwd"].value;
        this.setState({
            passwordStatus: true,
            invalidMsg: null,
            emailStatus: true,
        });
    
        if(this.verifyEmailAddress(email)){
            if(this.verifyPassword(password, confirmPwd)){
                this.props.onUpdateAccountsList(userName, email, password);
                this.props.toggleNested();
            }
        }
    }

    render(){
        return(
            <div>
                <Modal isOpen={this.props.modal} toggle={this.props.toggle} onClosed={this.clearFormMsg}>
                    <ModalHeader toggle={this.props.toggle}>
                        Sign Up
                    </ModalHeader>
                    <ModalBody>
                        <form onSubmit={this.handleSubmit}>
                            <FormInput icon="user" type="text" placeholder="username" name="userName"/>
                            <FormInput icon="envelope" type="email" placeholder="email" name="email"/>
                            <InvalidMsg validStatus={this.state.emailStatus} invalidMsg={this.state.invalidMsg} />
                            <FormInput icon="key" type="password" placeholder="password" name="password" />
                            <InvalidMsg validStatus={this.state.passwordStatus} invalidMsg={this.state.invalidMsg} />
                            <FormInput icon="key" type="password" placeholder="confirm password" name="confirmPwd" />
                            <div className="form-group">
                                <input type="submit" value="Sign Up" className="btn button" />
                            </div>
                        </form>
                        <ModalComponent isOpen={this.props.nestedModal} 
                            messageTitle="Register Successfully" messageContent="Congratulations! You have successfully registered an account."
                            toggle={this.props.toggleNested} onButtonClick={this.props.toggleAll} 
                            onClosed={this.props.closeAll ? this.props.toggle : undefined} />
                    </ModalBody>
                    <ModalFooter>
                        <a href="#" className="float-right">Forgot password?</a>
                    </ModalFooter>
                </Modal>
            </div>
        );
    }
}

export default Register;