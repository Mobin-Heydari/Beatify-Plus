"use client";

import React from "react";
import { useState } from "react";


export default function LandingNavbar() {

    const  [isOpen, setIsOpen] = useState(false);

    const toggleMenu = () => {
        setIsOpen(!isOpen);
      };


    return (
        <nav className="landing-navbar">
            <div className="logo-container">
                <div className="logo">
                    <a href="/">
                        <img src="assets/images/icons/beat.png" alt="Beatify Plus" />
                    </a>
                </div>
            </div>
            <div className="search-bar">
                <input type="text" placeholder="....." className="search-input"/>
            </div>
            <div className="navigation-bar">
                <ul className="nav-links">
                    <li className="nav-link">
                        <a href="/Home">
                            پلتفرم
                            <img src="assets/images/icons/home.png" alt="home" />
                        </a>
                    </li>
                    <li className="nav-link">
                        <a href="/Beats">
                            بیت ها
                            <img src="assets/images/icons/beat.png" alt="beats" />
                        </a>
                    </li>
                    <li className="nav-link">
                        <a href="/Musics">
                            موزیک ها
                            <img src="assets/images/icons/musics.png" alt="musics" />
                        </a>
                    </li>
                </ul>
            </div>
            <div className={isOpen === false ? "drop-down inactive" : "drop-down active"}>
                <div className="drop-down-icon" onClick={() => toggleMenu()}>
                    <img src="assets/images/icons/menu.png" alt="menu" />
                </div>
                <ul className="drop-down-items">
                    <li>
                        <p>پلتفرم</p>
                        <img src="assets/images/icons/home.png" alt="home" />
                    </li>
                    <li>
                        <p>بیت ها</p>
                        <img src="assets/images/icons/beat.png" alt="beats" />
                    </li>
                    <li>
                        <p>موزیک ها</p>
                        <img src="assets/images/icons/musics.png" alt="musics" />
                    </li>
                </ul>
            </div>
        </nav>
    )
}