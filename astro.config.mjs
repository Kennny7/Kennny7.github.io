// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://kennny7.github.io',
  base: '/',
  integrations: [tailwind()],
  build: {
    assets: 'assets',
    inlineStylesheets: 'auto'
  }
});