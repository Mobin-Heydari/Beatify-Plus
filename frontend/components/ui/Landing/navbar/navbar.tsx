"use client";

import React from "react";


export default function LandingNavbar() {
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
                <input type="text" placeholder="سرچ..." className="search-input"/>
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
        </nav>
    )
}