import 'bootstrap/dist/css/bootstrap.min.css';
import 'font-awesome/css/font-awesome.min.css';
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Login from './Component/Login';
import './index.css';
import './TicTac.css';
import './login.css';
import './signup.css';
import  {library} from '@fortawesome/fontawesome-svg-core';
import  {faUser, faKey, faEnvelope} from '@fortawesome/free-solid-svg-icons';

library.add(faUser, faKey, faEnvelope);

ReactDOM.render(<Login />, document.getElementById('root'));

