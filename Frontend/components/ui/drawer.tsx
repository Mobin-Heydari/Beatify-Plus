import React from "react";

import SideBar from "./sidebar";


export default function Drawer() {
    return (
        <div className="drawer drawer-menu">
            <input id="my-drawer" type="checkbox" className="drawer-toggle" />
            <div className="btn btn-ghost btn-circle">
                {/* Page content here */}
                <label htmlFor="my-drawer">
                    <img src="assets/images/icons/menu.png" alt="menu" className=""/>
                </label>
            </div>
            <SideBar />
        </div>
    )
}