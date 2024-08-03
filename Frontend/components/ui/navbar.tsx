"use client";

import React from "react";
import { useState } from "react";

import CartDropDown from "./navbar-cart-dropdown";


export default function NavBar() {

    const [closeMenu, setCloseMenu] = useState(true)
    const HandelCloseMenu = () => {
        setCloseMenu(!closeMenu)
    }

    return (
        <nav className="navbar">
            <div className="searchbar-contaner">

            </div>
            <div className="user-container">
            
            </div>
            <div className="mobile-sidebar-trigger" onClick={() => {HandelCloseMenu()}}>
            </div>
            <CartDropDown />
        </nav>
    )

}