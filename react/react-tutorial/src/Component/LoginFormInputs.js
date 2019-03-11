import React, {Component} from 'react';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';

function LoginFormInputs(props){
    return (
        <div>
            <div className="input-group form-group">
                <div className="input-group-prepend">
                    <span className="input-group-text"><FontAwesomeIcon icon="user" /></span>
                </div>
                <input type="text" className="form-control" placeholder="username" />
            </div>
            <div className="input-group form-group">
                <div className="input-group-prepend">
                    <span className="input-group-text"><FontAwesomeIcon icon="key" /></span>
                </div>
                <input type="password" className="form-control" placeholder="password" />
            </div>
            <div className="row align-items-center remember">
                <input type="checkbox" />Remember Me
            </div>
            <div className="form-group">
                <input type="submit" value={props.buttonName} className="btn float-right login_btn" />
            </div>
        </div>
    );
}

export default LoginFormInputs;