import React from "react";



export default function MainDropDown() {
    return (

        <div className="navbar-start lg:hidden">
            <div className="dropdown">
                <div tabIndex={0} role="button" className="btn btn-ghost btn-circle">
                    <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-5 w-5"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="M4 6h16M4 12h16M4 18h7" />
                    </svg>
                </div>
                <ul tabIndex={0} className="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow">
                    <li>
                        <a>خانه</a>
                    </li>
                    <li>
                        <a>ترک ها</a>
                    </li>
                    <li>
                        <a>تماس با ما</a>
                    </li>
                </ul>
            </div>
        </div>
    )
}