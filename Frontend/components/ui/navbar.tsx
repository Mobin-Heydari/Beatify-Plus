import React from "react";

import ProfileDropDown from "./profileDropDown";
import CartDropDown from "./cart-dropdown";
import SearchBar from "./searchbar";
import Drawer from "./drawer";


export default function Navbar() {
    return (
        <nav className="navbar">
            <Drawer />
            <SearchBar />
            <div className="dorp-down-nav-contents">
                <CartDropDown />
                <ProfileDropDown />   
            </div>
        </nav>
    );
  }
  