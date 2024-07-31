"use client";


import React from "react";
import { useState } from "react";
import { useLocation } from "react-router";




export default function MainSideBar() {

    const location = useLocation

    const [closeMenu, setCloseMenu] = useState(true)

    console.log(closeMenu)

    const HandelCloseMenu = () => {
        setCloseMenu(!closeMenu)
    }

    return (
        <aside className={closeMenu === false ? "sidebar" : "sidebar active"}>
            <div className="logo-container">
                <img src="assets/images/icons/beat.png" alt="logo" />
                <h2>Beatify Plus</h2>
            </div>
            <div className="burger-container">
                <div className="burger-trigger" onClick={()=>{HandelCloseMenu()}}></div>
                <div className="burger-menu"></div>
            </div>
            <div className="profile-container">
                <img src="assets/images/User.png" alt="user" />
                <div className="profile-content">
                    <p className="name">john</p>
                    <p className="email">szpm@gmail.com</p>
                </div>
            </div>
            <div className="content-container">
                <ul>
                    <li className="active">
                        <img src="assets/images/icons/album.png" alt="album" />
                        <a href="">album</a>
                    </li>
                    <li>
                        <img src="assets/images/icons/beat.png" alt="beat" />
                        <a href="">beat</a>
                    </li>
                    <li>
                        <img src="assets/images/icons/musics.png" alt="musics" />
                        <a href="">musics</a>
                    </li>
                    <li>
                        <img src="assets/images/icons/micro.png" alt="singer" />
                        <a href="">singer</a>
                    </li>
                    <li>
                        <img src="assets/images/icons/guitar.png" alt="musician" />
                        <a href="">musician</a>
                    </li>
                </ul>
            </div>
        </aside>
    )
}