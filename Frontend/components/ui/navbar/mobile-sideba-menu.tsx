"use client";

import React from "react";
import { useState, useContext } from "react";

import sidebarContext from "@/contexts/sidebar-context";


export default function MobileSidebarMenu() {
    const context = useContext(sidebarContext);
    
    if (!context) {
        throw new Error("Sidebar context is not provided");
    }

    return (
        <div className="mobile-sidebar-menu" onClick={() => {context.toggleSidebar()}}>
            <img src="assets/images/icons/menu.png" alt="menu" />
        </div>
    )
}