import React, {Component} from 'react';
import FormInput from './FormInput';
import { Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';

class Register extends Component{
    constructor(props){
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(e){
        //alert(e.target["userName"].value);
    }

    render(){
        return(
            <Modal isOpen={this.props.modal} toggle={this.props.toggle}>
                <ModalHeader toggle={this.props.toggle}>
                        Sign Up
                </ModalHeader>
                <ModalBody>
                    <form onSubmit={this.handleSubmit}>
                        <FormInput icon="user" type="text" placeholder="username" name="userName"/>
                        <FormInput icon="envelope" type="email" placeholder="email" name="email"/>
                        <FormInput icon="key" type="password" placeholder="password" name="password" />
                        <FormInput icon="key" type="password" placeholder="confirm password" name="confirmPwd" />
                        <div className="form-group">
                            <input type="submit" value="Sign Up" className="btn signup-button" />
                        </div>
                    </form>
                </ModalBody>
                <ModalFooter>
                    <a href="#" className="float-right">Forgot password?</a>
                </ModalFooter>
            </Modal>
        );
    }
}

export default Register;