import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "@uploadthing/react/styles.css";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "LearnForge Admin",
  description: "Admin interface to make changes to data in LearnForge",
};

import { NextSSRPlugin } from "@uploadthing/react/next-ssr-plugin";
import { extractRouterConfig } from "uploadthing/server";
 
import { ourFileRouter } from "@/app/api/uploadthing/core";
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <NextSSRPlugin
          routerConfig={extractRouterConfig(ourFileRouter)}
        />
        {children}
      </body>
    </html>
  )
}