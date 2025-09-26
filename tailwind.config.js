import { fontFamily as _fontFamily } from 'tailwindcss/defaultTheme'

export const content = ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}']

export const theme = {
  extend: {
    colors: {
      primary: {
        100: '#E6F0FF',
        500: '#0066CC',
        600: '#0052A3',
      },
    },
    fontFamily: {
      sans: ['"Playfair Display"', ..._fontFamily.sans],
      serif: ['Inter', ..._fontFamily.serif],
    },
  },
}

export const plugins = [
  require('@tailwindcss/aspect-ratio'),
]
