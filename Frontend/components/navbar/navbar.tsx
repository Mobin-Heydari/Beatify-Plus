import React from "react";

import ProfileDropDown from "./profiledropdown";


export default function Navbar() {
    return (
        <nav className="navbar">
            <div className="search-bar">
                <i></i>
                <input type="text" placeholder="Search..."/>
            </div>
            <ProfileDropDown />
        </nav>
    );
  }
  