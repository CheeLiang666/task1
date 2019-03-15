import React from 'react';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';

function FormInput(props){
    return (
        <div className="input-group form-group">
            <div className="input-group-prepend">
                <span className="input-group-text"><FontAwesomeIcon icon={props.icon} /></span>
            </div>
            <input type={props.type} className="form-control" name={props.name} placeholder={props.placeholder} required/>
        </div>
    );
}

export default FormInput;