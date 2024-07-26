import React from "react";

import ProfileDropDown from "./profiledropdown";
import SearchBar from "./searchbar";

export default function Navbar() {
    return (
        <nav className="navbar">
            <SearchBar></SearchBar>
            <ProfileDropDown />
        </nav>
    );
  }
  