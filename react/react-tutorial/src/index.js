import 'bootstrap/dist/css/bootstrap.min.css';
import 'font-awesome/css/font-awesome.min.css';
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';
import './login.css';
import './signup.css';
import './home.css';
import './Component/NavigationBar/authNavigationBar.css';
import Firebase, { FirebaseContext } from './Component/Firebase';
import  {library} from '@fortawesome/fontawesome-svg-core';
import  {faUser, faKey, faEnvelope, faHome, faFile, faEdit, faSignOutAlt} from '@fortawesome/free-solid-svg-icons';

library.add(faUser, faKey, faEnvelope, faHome, faFile, faEdit, faSignOutAlt);

ReactDOM.render(
    <FirebaseContext.Provider value={new Firebase()}>
        <App />
    </FirebaseContext.Provider>
    , document.getElementById('root'));

