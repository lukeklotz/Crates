import type { Metadata } from 'next';
import { Space_Grotesk, IBM_Plex_Mono } from 'next/font/google';
import './globals.css';
const sans = Space_Grotesk({
  variable: '--font-interface',
  subsets: ['latin'],
});
const mono = IBM_Plex_Mono({
  variable: '--font-label',
  subsets: ['latin'],
  weight: ['400', '500'],
});
export const metadata: Metadata = {
  title: 'Crate / Sandbox',
  description:
    'A workspace for your next listening direction. Search, arrange, and group albums.',
};
export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body className={`${sans.variable} ${mono.variable}`}>{children}</body>
    </html>
  );
}
