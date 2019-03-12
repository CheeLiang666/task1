import React from 'react';

function InvalidMsg(props){

    const validStatus = props.validStatus;
    const invalidMsg = props.invalidMsg;
    if(validStatus){
        return null;
    }
    return (<label className="invalidMsg">{invalidMsg}</label>);
}

export default InvalidMsg;