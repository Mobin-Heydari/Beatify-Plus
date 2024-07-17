import type { Metadata } from "next";

import Navbar from '@/components/navbar/navbar';

import "./globals.css";

export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" data-theme="dracula" dir="rtl">
      <body>
        <Navbar />
        {children}
      </body>
    </html>
  );
}
