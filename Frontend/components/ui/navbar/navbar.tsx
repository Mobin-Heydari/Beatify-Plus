"use client";

import React from "react";

import CartDropDown from "./cart-dropdown";
import MobileSidebarMenu from "./mobile-sideba-menu";


export default function NavBar() {

  return (
    <nav className="navbar">
        <MobileSidebarMenu />
        <div className="searchbar-contaner"></div>
        <div className="user-container"></div>
        <CartDropDown />
    </nav>
  );
}
