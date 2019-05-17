import React, {Component} from 'react';
import NavLink from './NavLink';

function NavigationBar(props){

    return (
        <nav className='navbar navbar-expand-lg fixed-top navbar-dark bg-primary'>
            <button className='navbar-toggler' type='button' data-toggle='collapse' 
                data-target='#navbarToggler' aria-controls='navbarToggler' aria-expanded='false'
                aria-label='Toggle navigation'>
                <span className='navbar-toggler-icon'></span>
            </button>
            <div className='collapse navbar-collapse' id='navbarToggler'>
            <div className='navbar-brand'>
                ReactProject
            </div>
                <ul className='nav navbar-nav mr-auto'>
                    <NavLink name='Home'/>
                    <NavLink name='About' />
                </ul>
                <ul className='nav navbar-nav navbar-right'>
                    <NavLink name='Login' />
                </ul>
            </div>
        </nav>
    )
}

export default NavigationBar;