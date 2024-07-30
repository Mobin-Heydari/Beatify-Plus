import React from "react";



export default function SideBar() {
    return (
        <aside className="drawer-side hover">
            <label htmlFor="my-drawer" aria-label="close sidebar" className="drawer-overlay"></label>
            <ul className="menu bg-primary">
                <li><a>Sidebar Item 1</a></li>
                <li><a>Sidebar Item 2</a></li>
            </ul>
        </aside>
    )
}