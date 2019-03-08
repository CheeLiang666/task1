import React from 'react';

function NavLink(props){
    return (
        <li className={`nav-item ${props.activeStatus}`}>
            <a className='nav-link' href='#'>{props.name}</a>
        </li>
    )
}

export default NavLink;