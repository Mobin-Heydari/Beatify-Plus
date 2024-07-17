import React from "react";
import MainDropDown from "./mainDropDown";
import NavigatingBar from "./navItems";
import ProfileDropDown from "./profileDropDown";
import CartDropDown from "./cart";


export default function Navbar() {
    return (
        <nav className="navbar bg-base-100">
            <NavigatingBar />
            <MainDropDown />
            <div className="navbar-end">
                <CartDropDown />
                <ProfileDropDown />
            </div>
        </nav>
    );
  }
  