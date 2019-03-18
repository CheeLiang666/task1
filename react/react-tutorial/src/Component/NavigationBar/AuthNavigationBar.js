import React from 'react';
import {
    Collapse, Navbar, NavbarToggler, NavbarBrand,
    Nav, NavItem, NavLink, Dropdown, DropdownToggle,
    DropdownMenu, DropdownItem } from 'reactstrap';
import {withFirebase} from '../Firebase';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'

class NavigationBar extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            isOpen: false,
            dropDownOpen: false,
        };
        this.toggleNav = this.toggleNav.bind(this);
        this.toggleDropdown = this.toggleDropdown.bind(this);
    }

    toggleNav(){
        this.setState({
            isOpen: !this.state.isOpen,
        });
    }
    
    toggleDropdown(){
        this.setState({
            dropDownOpen: !this.state.dropDownOpen,
        });
    }

    render(){
        return(
            <div>
                <Navbar className="fixed-top" color="dark" dark expand="md">
                    <NavbarBrand href="#">Blog</NavbarBrand>
                    <NavbarToggler onClick={this.toggleNav} />
                    <Collapse isOpen={this.state.isOpen} navbar>
                        <Nav className="mr-auto" navbar>
                            <NavItem>
                                <NavLink href="#">
                                    <FontAwesomeIcon icon="home" className="right-padding" size="lg"/>Home
                                </NavLink>
                            </NavItem>
                            <NavItem>
                                <NavLink href="#">
                                    <FontAwesomeIcon icon="edit" className="right-padding" size="lg"/>Create Post
                                </NavLink>
                            </NavItem>
                        </Nav>
                        <Nav className="ml-auto" navbar>
                            <Dropdown className="active" isOpen={this.state.dropDownOpen} toggle={this.toggleDropdown} nav inNavbar>
                                <DropdownToggle nav caret>
                                <FontAwesomeIcon icon="user" className="right-padding" size="lg"/>
                                    {this.props.authUserName}
                                </DropdownToggle>
                                <DropdownMenu right>
                                    <DropdownItem>
                                        <FontAwesomeIcon icon="file" className="right-padding" size="lg"/>Profile
                                    </DropdownItem>
                                    <DropdownItem divider />
                                    <DropdownItem onClick={this.props.firebase.doSignOut}>
                                        <FontAwesomeIcon icon="sign-out-alt" className="right-padding" size="lg"/>Logout
                                    </DropdownItem>
                                </DropdownMenu>
                            </Dropdown>
                        </Nav>
                    </Collapse>
                </Navbar>
            </div>
        );
    }
}

export default withFirebase(NavigationBar);