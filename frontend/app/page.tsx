"use client";

import { useState } from "react";

import "./globals.css";
import sidebarContext from "@/contexts/sidebar-context";
import NavBar from "@/components/ui/navbar/navbar";
import MainSideBar from "@/components/ui/sidebar";

export default function Home() {
  const [sidebarStatus, setSidebarStatus] = useState(true);

  const toggleSidebar = () => {
    setSidebarStatus(!sidebarStatus);
  };

  return (
    <sidebarContext.Provider value={{ sidebarStatus, toggleSidebar }}>
      <NavBar />
      <MainSideBar />
      <main></main>
    </sidebarContext.Provider>
  );
}
