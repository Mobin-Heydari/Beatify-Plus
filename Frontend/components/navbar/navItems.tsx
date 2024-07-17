import React from "react";




export default function NavigatingBar() {
    return (
        <div className="navbar-start hidden lg:flex">
            <ul className="menu menu-horizontal px-1">
                <li><a>خانه</a></li>
                <li>
                    <details>
                    <summary>ترک ها</summary>
                    <ul className="p-2">
                        <li><a>پرطرفدار ترین ها</a></li>
                        <li><a>بیشترین پلی ها</a></li>
                    </ul>
                    </details>
                </li>
                <li><a>تماس با ما</a></li>
            </ul>
        </div>
    )
}