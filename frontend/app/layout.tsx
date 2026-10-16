import type { Metadata } from 'next';
import { IBM_Plex_Mono, Pixelify_Sans } from 'next/font/google';
import './globals.css';
const mono = IBM_Plex_Mono({
  variable: '--font-interface',
  subsets: ['latin'],
  weight: ['400', '500', '600', '700'],
});
const display = Pixelify_Sans({
  variable: '--font-display',
  subsets: ['latin'],
});
export const metadata: Metadata = {
  title: 'crates / sandbox',
  description:
    'a workspace for finding your next favorite record. search, arrange, and group albums',
};
export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body className={`${mono.variable} ${display.variable}`}>{children}</body>
    </html>
  );
}
