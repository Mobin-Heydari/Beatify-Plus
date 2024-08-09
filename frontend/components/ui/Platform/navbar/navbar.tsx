"use client";

import React from "react";

import CartDropDown from "./cart-dropdown";
import MobileSidebarMenu from "./mobile-sideba-menu";
import ProfileDropDown from "./profile";


export default function NavBar() {

  return (
    <nav className="navbar">
        <MobileSidebarMenu />
        <ProfileDropDown />
        <CartDropDown />
    </nav>
  );
}
