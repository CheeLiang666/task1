import React, {Component} from 'react';
import FormInput from '../FormInput';
import InvalidMsg from './InvalidMsg';
import ModalComponent from '../ModelComponent';
import { Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';
import {withFirebase} from '../../Firebase';

const initialState = {
    invalidMsg: null,
};

class Register extends Component{
    constructor(props){
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.state = {
            invalidMsg: null,
        };
        this.verifyPassword = this.verifyPassword.bind(this);
        // this.verifyEmailAddress = this.verifyEmailAddress.bind(this);
        this.clearFormMsg = this.clearFormMsg.bind(this);
        this.resetToInitialState = this.resetToInitialState.bind(this);
    }

    resetToInitialState(){
        this.setState({...initialState});
    }

    // verifyEmailAddress(email){
    //     const accountsList = this.props.accountsList;
    //     for(let i = 0; i < accountsList.length; i++){
    //         if(email === accountsList[i].email){
    //             this.setState({
    //                 emailStatus: false,
    //                 invalidMsg: "Email had already been registered.",
    //             });
    //             return false;
    //         }else{
    //             continue;
    //         }
    //     }
    //     this.setState({
    //         emailStatus: true,
    //         invalidMsg: null,
    //         passwordStatus: true,
    //     });
    //     return true;
    // }

    verifyPassword(password, confirmPwd){
        if(password === confirmPwd){
            this.setState({
                invalidMsg: null,
            });
            return true;
        }else{
            this.setState({
                invalidMsg: "Password and confirm password not match.",
            });
            return false;
        }
    }

    clearFormMsg(){
        this.setState({
            invalidMsg: null,
        });
    }

    handleSubmit(e){
        e.preventDefault();
        this.resetToInitialState();
        const userName = e.target["userName"].value;
        const email = e.target["email"].value;
        const password = e.target["password"].value;
        const confirmPwd = e.target["confirmPwd"].value;
    
        // if(this.verifyEmailAddress(email)){
        //     if(this.verifyPassword(password, confirmPwd)){
        //         this.props.onUpdateAccountsList(userName, email, password);
        //         this.props.toggleNested();
        //     }
        // }
        if(this.verifyPassword(password, confirmPwd)){
            this.props.firebase
            .doCreateUserWithEmailAndPassword(email, password)
            .then(authUser => {
                //Create a user in the Firebase realtime database
                return this.props.firebase
                .user(authUser.user.uid)
                .set({
                    userName,
                    email,
                });
            })
            .then(() => {
                //success
                this.props.toggleNested();
            })
            .catch(error => {
                this.setState({invalidMsg: error.message});
                console.log(error);
            });
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
                            <FormInput icon="key" type="password" placeholder="password" name="password" />
                            <FormInput icon="key" type="password" placeholder="confirm password" name="confirmPwd" />
                            <InvalidMsg invalidMsg={this.state.invalidMsg} />
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

export default withFirebase(Register);