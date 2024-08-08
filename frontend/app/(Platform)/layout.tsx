import type { Metadata } from "next";

import "./style.css";

export const metadata: Metadata = {
  title: "Beatify Plus | Platform",
  description: "Beatify Plus music platform",
};

interface SidebarContextValue {
  sidebarStatus: boolean;
  toggleSidebar: () => void;
}

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="fa" dir="rtl">
      <head>
      </head>
      <body>
        {children}
      </body>
    </html>
  );
}