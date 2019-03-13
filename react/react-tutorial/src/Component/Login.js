import React, {Component} from 'react';
import FormInput from './FormInput';
import Register from './Register';
import ModalComponent from './ModelComponent';
import auth from './auth';

class Login extends Component{
    constructor(props){
        super(props);
        this.state = {
            signUpModal: false,
            nestedSignUpModal: false,
            closeAll: false,
            loginModal: false,
            success: false,
            account:[
                {
                    userName: "Alice",
                    email: "alice@email.com",
                    password: "1233",
                },
            ],
        };
        this.toggleLoginModal = this.toggleLoginModal.bind(this);
        this.toggleSignUpModal = this.toggleSignUpModal.bind(this);
        this.updateAccountsList = this.updateAccountsList.bind(this);
        this.toggleNestedSignUp = this.toggleNestedSignUp.bind(this);
        this.toggleAllSignUpModals = this.toggleAllSignUpModals.bind(this);
        this.verifyLoginInput = this.verifyLoginInput.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.login = this.login.bind(this);
        this.handleLoginModalSuccessClickEvent = this.handleLoginModalSuccessClickEvent.bind(this);
    }

    toggleLoginModal(){
        this.setState({
            loginModal: !this.state.loginModal,
        });
    }

    toggleNestedSignUp(){
        this.setState({
            nestedSignUpModal: !this.state.nestedSignUpModal,
            closeAll: false,
        });
    }

    toggleAllSignUpModals(){
        this.setState({
            nestedSignUpModal: !this.state.nestedSignUpModal,
            closeAll: true,
        });
    }

    toggleSignUpModal(){
        this.setState({
            signUpModal: !this.state.signUpModal,
        })
    }

    updateAccountsList(userName, email, password){
        const account = this.state.account.slice();
        const newAccount = {userName: userName, email: email, password: password};
        this.setState({
            account: account.concat(newAccount),
        });
    }

    verifyLoginInput(currentAccount, accountsList){
        for(let i = 0; i < accountsList.length; i++){
            if(currentAccount.email === accountsList[i].email && currentAccount.password === accountsList[i].password){
                this.setState({
                    success: true,
                });
                return true;
            }else{
                continue;
            }
        }
        this.setState({
            success: false,
        });
        return false;
    }

    handleSubmit(e){
        e.preventDefault();
        const accountsList= this.state.account.slice();
        const currentAccount = {
            email: e.target["email"].value,
            password: e.target["password"].value,
        };
        if(this.verifyLoginInput(currentAccount, accountsList)){
            this.toggleLoginModal();
        }else{
            this.toggleLoginModal();
        }
    }

    handleLoginModalSuccessClickEvent(e){
        this.login();
    }

    login(){
        auth.login(() => {
            this.props.history.push("/home");
        });
    }

    render(){
        const accountsList = this.state.account.slice();
        const currentAccount = accountsList[accountsList.length - 1];
        const success = this.state.success;
        let messageTitle = (success) ? "Login Successfully" : "Failed to login";
        let messageContent = (success) ? "Welcome " + currentAccount.userName + "!" : "Invalid email address or password.";

        return(
            <div className="container-fluid login">
                <ModalComponent isOpen={this.state.loginModal} 
                    messageTitle={messageTitle} messageContent={messageContent}
                    toggle={this.toggleLoginModal} onClosed={(success) ? this.login : undefined} 
                    onButtonClick={(success) ? this.handleLoginModalSuccessClickEvent : this.toggleLoginModal}/>
                
                <Register modal={this.state.signUpModal} toggle={this.toggleSignUpModal} accountsList={this.state.account}
                        onUpdateAccountsList={this.updateAccountsList}
                        nestedModal={this.state.nestedSignUpModal} toggleNested={this.toggleNestedSignUp}
                        closeAll={this.state.closeAll} toggleAll={this.toggleAllSignUpModals}/>
                <div className="d-flex justify-content-end h-100">
                    <div className="card">
                        <div className="card-header">
                            <h3>Sign In</h3>
                        </div>
                        <div className="card-body">
                            <form onSubmit={this.handleSubmit}>
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
                                Don't have an account?<a href="#" onClick={this.toggleSignUpModal}>Sign Up</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Login;