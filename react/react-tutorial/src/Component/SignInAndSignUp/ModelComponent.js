import React from 'react';
import { Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';

function ModalComponent(props){
    return (
        <Modal isOpen={props.isOpen} toggle={props.toggle} onClosed={props.onClosed}>
            <ModalHeader>{props.messageTitle}</ModalHeader>
            <ModalBody>{props.messageContent}</ModalBody>
            <ModalFooter>
                <button className="btn button" onClick={props.onButtonClick}>Close</button>
            </ModalFooter>
        </Modal>
    );
}

export default ModalComponent;
