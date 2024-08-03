"use client";

import React from "react";
import { useState, useContext  } from "react";

import CartDropDown from "./navbar-cart-dropdown";
import sidebarContext from "@/contexts/sidebar-context";


export default function NavBar() {

    const context = useContext(sidebarContext)

    if (!context) {
        throw new Error("Sidebar context is not provided");
    }

    return (
        <nav className="navbar">
            <div className="mobile-sidebar-menu" onClick={() => {context.toggleSidebar()}}>
                <img src="assets/images/icons/menu.png" alt="menu" />
            </div>
            <div className="searchbar-contaner">

            </div>
            <div className="user-container">
            
            </div>
            <CartDropDown />
        </nav>
    )

}