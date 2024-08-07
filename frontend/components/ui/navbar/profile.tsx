"use client";

import React from "react";
import { useRouter } from 'next/navigation'


export default function ProfileDropDown() {

    const router = useRouter()

    return (
        <div className="profile-container">
            <div className="icon" onClick={() => router.push('/dashboard')}>
                <img src="assets/images/User.png" alt="User" />
            </div>
        </div>
    )
}