import React from "react";



export default function CartDropDown() {
    return (
        <div className="dropdown dropdown-end">
            <div tabIndex={0} role="button" className="btn btn-ghost btn-circle">
                <div className="indicator">
                <img src="assets/images/icons/cart.png" alt="" />
                <span className="badge badge-sm indicator-item bg-primary border-primary">2</span>
                </div>
            </div>
            <div tabIndex={0} className="card card-compact dropdown-content cart-dropdown-items">
                <div className="card-body">
                    <span className="item-count">2 آیتم</span>
                    <span className="total-price">قیمت کل: 120/000/000 تومان</span>
                    <div className="buttons">
                        <div className="card-actions">
                            <a href="cart/" className="view btn">مشاهده</a>
                        </div>
                        <div className="card-actions">
                            <a href="cart/" className="pay btn">پرداخت</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}