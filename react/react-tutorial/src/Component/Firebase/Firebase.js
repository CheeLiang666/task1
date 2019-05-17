import app from 'firebase/app';
import 'firebase/auth';
import 'firebase/database';

const config = {
    apiKey: "AIzaSyB3r-fw-XWO_-WFtmXi0tNlqbcZ_x_m33M",
    authDomain: "reactproject1-4b254.firebaseapp.com",
    databaseURL: "https://reactproject1-4b254.firebaseio.com",
    projectId: "reactproject1-4b254",
    storageBucket: "reactproject1-4b254.appspot.com",
    messagingSenderId: "540122497096"
  };

class Firebase {
    constructor(){
        app.initializeApp(config);
        this.auth = app.auth();
        this.db = app.database();
    }

    //Auth API (These endpoints are called asynchronously)
    doCreateUserWithEmailAndPassword = (email, password) => this.auth.createUserWithEmailAndPassword(email, password);

    doSignInWithEmailAndPassword = (email, password) => this.auth.signInWithEmailAndPassword(email, password);

    doSignOut = () => this.auth.signOut();

    doPasswordReset = email => this.auth.sendPasswordResetEmail(email);
    doPasswordUpdate = password => this.auth.currentUser.updatePassword(password);

    //User API
    user = uid => this.db.ref(`users/${uid}`);
    users = () => this.db.ref('users');
}

export default Firebase;