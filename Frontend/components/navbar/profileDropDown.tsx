import React from "react";
  

export default function ProfileDropDown() {
    return (
        <div className="dropdown dropdown-end">
            <div tabIndex={0} role="button" className="btn btn-ghost btn-circle">
                <div className="w-10 rounded-full">
                    <img alt="User Profile"  src="assets/images/User.png" />
                </div>
            </div>
            <ul tabIndex={0} className="menu dropdown-content profile-drop-down-items">
                <li className="profile-section">
                    <div>
                        <div className="profile-avatar">
                            <a href="/">
                              <img alt="User Profile"  src="assets/images/User.png"/>
                            </a>
                        </div>
                        <div className="username">
                          <span className="text-xxl">
                            <a href="/">
                              نام کاربری 
                            </a>
                          </span>
                        </div>
                    </div>
                </li>
                <div className="divider divider-secondary"></div>
                <li className="navbar-items">
                    <a href="/">
                        <img src="/assets/images/icons/settings.png" alt="settings" />
                        <p>تنظیمات</p>
                    </a>
                    <a href="/">
                        <img src="/assets/images/icons/wallet.png" alt="wallet" />
                        <p>کیف پول</p>
                    </a>
                    <a href="/">
                        <img src="/assets/images/icons/orders.png" alt="orders" />
                        <p>سفارشات</p>
                    </a>
                </li>
                <div className="divider divider-secondary"></div>
                <li className="navbar-items">
                    <a href="/">
                        <img src="/assets/images/icons/resent.png" alt="resent"/>
                        <p>سابقه</p>
                    </a>
                    <a href="/">
                        <img src="/assets/images/icons/play-list.png" alt="play list"/>
                        <p>پلی لیست</p>
                    </a>
                    <a href="/">
                        <img src="/assets/images/icons/heart.png" alt="favorite"/>
                        <p>علاقه مندی</p>
                    </a>
                    <a href="/">
                        <img src="/assets/images/icons/save.png" alt="save"/>
                        <p>ذخیره شده</p>
                    </a>
                </li>
            </ul>
        </div>
    )
}

