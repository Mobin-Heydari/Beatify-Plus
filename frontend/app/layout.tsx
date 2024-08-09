import type { Metadata } from "next";

import "./globals.css";

export const metadata: Metadata = {
  title: "Beatify Plus",
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
    <html lang="fa" dir="ltr">
      <head>
      </head>
      <body>
        {children}
      </body>
    </html>
  );
}