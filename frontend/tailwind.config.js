/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'darukaa-green': '#1B4D3E',      // Deep forest green (like the logo/icons)
        'darukaa-light': '#F4F9F5',      // Soft background for chat bubbles & sidebar
        'darukaa-surface': '#FFFFFF',    // Pure white for cards
        'darukaa-border': '#EAEBEA',     // Very subtle borders
        'darukaa-text': '#2D3748',       // Dark readable text, not pure black
        'darukaa-muted': '#718096',      // For timestamps and subtle labels
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        serif: ['Playfair Display', 'serif'],
      },
      boxShadow: {
        'subtle': '0 4px 20px -2px rgba(0, 0, 0, 0.05)', // Premium soft shadow for cards
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}