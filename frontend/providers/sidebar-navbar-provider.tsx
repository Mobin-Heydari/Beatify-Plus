"use client";

import { useState } from "react";

import sidebarContext from "@/contexts/sidebar-context";
import NavBar from "@/components/ui/Platform/navbar/navbar";
import MainSideBar from "@/components/ui/Platform/sidebar";

export default function SidebarNavbarProvider() {
  const [sidebarStatus, setSidebarStatus] = useState(true);

  const toggleSidebar = () => {
    setSidebarStatus(!sidebarStatus);
  };

  return (
    <sidebarContext.Provider value={{ sidebarStatus, toggleSidebar }}>
      <NavBar />
      <MainSideBar />
    </sidebarContext.Provider>
  );
}