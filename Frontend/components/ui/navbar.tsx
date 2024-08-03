"use client";

import React from "react";
import { useState } from "react";



export default function NavBar() {

    const [openCart, setOpenCart] = useState(false)
    const HandelOpenCart = () => {
        setOpenCart(!openCart)
    }

    console.log(openCart)

    const [closeMenu, setCloseMenu] = useState(true)
    const HandelCloseMenu = () => {
        setCloseMenu(!closeMenu)
    }

    return (
        <nav className="navbar">
            <div className="searchbar-contaner">

            </div>
            <div className="user-container">
            
            </div>
            <div className="mobile-sidebar-trigger" onClick={() => {HandelCloseMenu()}}>
            </div>
            <div className="cart-container">
                <div className="icon" onClick={() => {HandelOpenCart()}}>
                    <img src="assets/images/icons/cart.png" alt="" />
                </div>
                <div className={openCart === false ? "inactive-cart-drop-down" : "cart-drop-down"}>
                    <div className="cart-detail">
                        <div className="price">
                            <p>قیمت کل : <span>120/000 تومان</span></p>
                        </div>
                        <div className="quantity">
                            <p> تعداد : <span>10</span></p>
                        </div>
                    </div>
                    <div className="cart-actions">
                        <a href="cart/" className="view">
                            <p>مشاهده</p>
                            <img src="assets/images/icons/view.png" alt="" />
                        </a>
                        <a href="cart/pay/" className="pay">
                            <p> پرداخت</p>
                            <img src="assets/images/icons/payment.png" alt="" />
                        </a>
                    </div>
                </div>
            </div>
        </nav>
    )

}