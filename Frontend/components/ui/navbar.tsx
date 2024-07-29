import React from "react";

import ProfileDropDown from "./profileDropDown";
import SearchBar from "./searchbar";
import CartDropDown from "./cart-dropdown";


export default function Navbar() {
    return (
        <nav className="navbar">
            <SearchBar></SearchBar>
            <div className="dorp-down-nav-contents">
                <CartDropDown/>
                <ProfileDropDown />   
            </div>
        </nav>
    );
  }
  