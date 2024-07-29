import React from "react";



export default function SearchBar() {
    return (
        <label className="input search-bar">
            <img src="assets/images/icons/search.png" alt="search" />
            <input type="text" className="grow" placeholder="سرچ" />
        </label>
    )
}