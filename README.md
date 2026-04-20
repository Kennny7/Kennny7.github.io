
<div align="center">
  <h1>Khushal Pareta | MLOps Portfolio</h1>
  
  <p>
    <a href="https://github.com/Kennny7/Kennny7.github.io/actions"><img src="https://img.shields.io/github/actions/workflow/status/Kennny7/Kennny7.github.io/deploy.yml?style=for-the-badge&logo=githubactions&label=Deploy&color=06b6d4" alt="Deploy Status"></a>
    <a href="https://kennny7.github.io"><img src="https://img.shields.io/badge/Live-Site-06b6d4?style=for-the-badge&logo=astro" alt="Live Site"></a>
    <a href="https://github.com/Kennny7/Kennny7.github.io/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-06b6d4?style=for-the-badge" alt="License"></a>
  </p>
  
  <p>
    <sub>A modern, scalable portfolio template built with Astro and Tailwind CSS, designed for MLOps / Data / ML Engineers. Features content collections, GitHub repo stats fetching, and zero‑config deployment to GitHub Pages.</sub>
  </p>
</div>

---

### [>] Overview

This repository contains the source code for a **personal portfolio website** tailored to technical professionals in **MLOps, Data Engineering, and Machine Learning**. The site is statically generated using [Astro](https://astro.build), styled with [Tailwind CSS](https://tailwindcss.com), and automatically deployed to **GitHub Pages** via GitHub Actions.

**Why this template stands out:**

- **Content Collections** — Add new projects by creating a single Markdown file; no code changes required.  
- **Live GitHub Stats** — Optionally fetch repository stars, forks, and primary language at build time.  
- **Professional Aesthetic** — Dark theme, glassmorphism cards, monospace accents, and a clean terminal‑inspired design.  
- **Fully Responsive** — Mobile‑first layout that adapts seamlessly to any screen size.  
- **SEO & Social Ready** — Built‑in Open Graph and Twitter Card meta tags.  
- **Zero‑Cost Hosting** — Deploy to GitHub Pages with a single push.

---

### [>] Live Demo

**[+] [https://kennny7.github.io](https://kennny7.github.io)**

---

### [>] Features

<details open>
<summary><b>[+] Core Functionality</b></summary>

- **Dynamic Project Showcase** — Display projects as cards with images, descriptions, tech tags, and repository links.  
- **GitHub Integration** — Each project card can show live repository metrics (stars, forks, language) using the GitHub API.  
- **Skills Table** — Expandable/collapsible table grouping technologies by domain (Languages, Data Engineering, MLOps, Cloud, etc.).  
- **Impact Stats** — Highlight key metrics (e.g., "40% Faster Processing") with animated cards.  
- **Contact Section** — Integrated buttons for LinkedIn, GitHub, Email, and Phone.  
- **Education Timeline** — Clean presentation of academic credentials.  

</details>

<details>
<summary><b>[+] Developer Experience</b></summary>

- **Content Collections (Astro)** — Define projects in `src/content/projects/` using Markdown frontmatter.  
- **Type‑Safe** — Full TypeScript support with Zod schema validation.  
- **Fast Builds** — Astro's static generation ensures near‑instant page loads.  
- **Tailwind Utility Classes** — Rapid styling without leaving HTML.  
- **Pre‑configured Prettier** — Consistent code formatting out of the box.  

</details>

---

### [>] Tech Stack

| Layer          | Technology                                                                 |
|----------------|----------------------------------------------------------------------------|
| **Framework**  | [Astro](https://astro.build) v5                                            |
| **Styling**    | [Tailwind CSS](https://tailwindcss.com) v3                                 |
| **Language**   | TypeScript                                                                 |
| **Deployment** | GitHub Pages + GitHub Actions                                              |
| **Content**    | Astro Content Collections + Markdown                                       |
| **Icons**      | Custom SVG (Lucide‑inspired)                                               |
| **Fonts**      | Inter (sans), JetBrains Mono (mono)                                        |

---

### [>] Getting Started

#### Prerequisites

- Node.js `>=18.0.0`
- npm (or pnpm/yarn)

#### Installation

```bash
# Clone the repository
git clone https://github.com/Kennny7/Kennny7.github.io.git
cd Kennny7.github.io

# Install dependencies
npm install

# Start the development server
npm run dev
```

Visit `http://localhost:4321` to view the site locally. Changes are hot‑reloaded instantly.

#### Build for Production

```bash
npm run build
```

The output will be generated in the `dist/` directory.

---

### [>] Customization Guide

This template is designed to be easily adapted for your own portfolio. Follow the steps below to personalize every aspect.

<details open>
<summary><b>[+] 1. Personal Information</b></summary>

All personal details (name, contact links, skills, education, impact stats) are centralized in:

**`src/utils/constants.ts`**

| Export          | Purpose                                                                 |
|-----------------|-------------------------------------------------------------------------|
| `CONTACT`       | Email, phone, location, LinkedIn, GitHub URLs                            |
| `NAV_ITEMS`     | Navigation menu items                                                    |
| `SKILLS`        | Array of skill domains (domain name + array of technologies)             |
| `IMPACT_STATS`  | Key metric cards displayed on homepage (value + label)                   |
| `EDUCATION`     | Academic qualifications (degree, institution, year, score, highlight)    |

**Example: Updating Skills**

```typescript
export const SKILLS = [
  {
    domain: 'Languages',
    skills: ['Python', 'SQL', 'Bash'],
  },
  // Add or remove domains here
];
```

</details>

<details>
<summary><b>[+] 2. Adding a New Project</b></summary>

Projects are stored as **Markdown files** inside `src/content/projects/`. Each file has frontmatter that defines the project's metadata.

**Step‑by‑Step:**

1. Create a new `.md` file in `src/content/projects/` (e.g., `my-awesome-project.md`).

2. Add the following frontmatter at the top:

```markdown
---
title: "My Awesome Project"
description: "A concise description of what this project does."
image: "/images/projects/my-awesome.png"
github: "https://github.com/yourusername/your-repo"
demo: "https://demo-link.com"          # optional
tags: ["Python", "Spark", "AWS"]
featured: true                          # shows on homepage
fetchGithubData: true                   # fetches stars/forks/language from GitHub API
---
```

3. Place a screenshot of your project in `public/images/projects/` and reference it as `/images/projects/your-image.png`.

4. Optionally, write a detailed description below the frontmatter using standard Markdown (this content can be displayed on a dedicated project page if you choose to extend the template).

5. Save the file. The new project will appear automatically on the `/projects` page and (if `featured: true`) on the homepage.

**Notes:**

- `fetchGithubData: true` will make a request to the GitHub API **at build time**. If you have many projects, consider the [GitHub API rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api). For unauthenticated requests, the limit is 60 per hour per IP. You can increase this by providing a `GITHUB_TOKEN` environment variable (see Advanced Configuration).

</details>

<details>
<summary><b>[+] 3. Changing the Theme / Styling</b></summary>

The color palette and global styles are defined in two primary files:

| File                    | Purpose                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------|
| `tailwind.config.js`    | Tailwind theme extension: fonts, custom colors (HSL variables), animations, keyframes.     |
| `src/styles/global.css` | CSS custom properties (HSL values), base styles, utility classes (`.glass-card`, `.glow`). |

**Changing the Accent Color**

The primary accent color is a cyan/blue gradient. To change it, modify the HSL variables in `global.css`:

```css
:root {
  --primary: 186 100% 50%;   /* Hue Saturation Lightness - currently cyan */
  /* ... */
}
```

Example for a purple accent: `--primary: 270 100% 65%;`

**Adding Custom Fonts**

The template uses Google Fonts (Inter and JetBrains Mono) loaded in `global.css`. Replace the `@import` statement with your preferred fonts and update `tailwind.config.js` accordingly.

</details>

<details>
<summary><b>[+] 4. Updating the Header / Footer</b></summary>

- **Header**: `src/components/Header.astro` — Contains the logo, navigation, and mobile menu logic.  
- **Footer**: `src/components/Footer.astro` — Displays copyright, email, and social links.

Both components import `CONTACT` and `NAV_ITEMS` from `constants.ts`.

</details>

<details>
<summary><b>[+] 5. Modifying Page Content</b></summary>

| Page                | File Path                 | Editable Sections                                                  |
|---------------------|---------------------------|--------------------------------------------------------------------|
| Homepage            | `src/pages/index.astro`   | Hero text, impact stats grid, skills section, education timeline.  |
| Projects Gallery    | `src/pages/projects.astro`| Page header, project grid layout.                                  |
| Contact Page        | `src/pages/contact.astro` | Contact methods display.                                           |

All pages are standard Astro components; you can freely rearrange or add sections using HTML/Tailwind and Astro's templating syntax.

</details>

---

### [>] Deployment to GitHub Pages

This project includes a **GitHub Actions workflow** that automatically builds and deploys the site to GitHub Pages whenever you push to the `main` branch.

<details open>
<summary><b>[+] Step‑by‑Step Deployment</b></summary>

1. **Fork or push this repository** to your own GitHub account (ensure the repository name is exactly `<username>.github.io` for a user/organization site).

2. **Verify the workflow file** exists at `.github/workflows/deploy.yml`. It uses the official `withastro/action` to build and `actions/deploy-pages` to deploy.

3. **Enable GitHub Pages** in your repository settings:
   - Navigate to **Settings > Pages**.
   - Under "Build and deployment", select **"GitHub Actions"** as the source.

4. **Push a commit** to the `main` branch. The workflow will trigger automatically.

5. **Monitor the deployment** under the **Actions** tab. Once completed, your site will be live at `https://<username>.github.io`.

</details>

<details>
<summary><b>[+] Custom Domain</b></summary>

To use a custom domain:
1. Add a `CNAME` file in the `public/` directory containing your domain (e.g., `www.yourdomain.com`).
2. Configure your DNS provider as described in [GitHub's documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).
3. Update the `site` field in `astro.config.mjs` to match your custom domain.

</details>

---

### [>] Project Structure

<details>
<summary><b>[+] Full Directory Tree (click to expand)</b></summary>

```
kennny7.github.io/
├── .github/
│   └── workflows/
│       └── deploy.yml                 # GitHub Actions build & deploy pipeline
├── public/                            # Static assets (copied as‑is)
│   ├── favicon.svg
│   └── images/
│       └── projects/                  # Store project screenshots here
│           ├── aws-surveillance.png
│           └── azure-crime.png
├── src/
│   ├── components/                    # Reusable Astro components
│   │   ├── ContactButtons.astro
│   │   ├── Footer.astro
│   │   ├── Header.astro
│   │   └── ProjectCard.astro
│   ├── content/                       # Astro Content Collections
│   │   ├── config.ts                  # Schema definition for projects
│   │   └── projects/                  # Markdown files for each project
│   │       ├── aws-surveillance.md
│   │       └── azure-crime.md
│   ├── layouts/                       # Page layout wrappers
│   │   └── BaseLayout.astro
│   ├── pages/                         # File‑based routing
│   │   ├── index.astro                # Homepage
│   │   ├── projects.astro             # All projects gallery
│   │   └── contact.astro              # Contact page
│   ├── styles/
│   │   └── global.css                 # Tailwind imports + custom CSS
│   └── utils/
│       ├── constants.ts               # Personal data & configuration
│       └── github.ts                  # GitHub API fetch utility
├── .gitignore
├── .prettierrc
├── astro.config.mjs                   # Astro configuration
├── package.json
├── tailwind.config.js
├── tsconfig.json
└── README.md                          # This file
```

</details>

---

### [>] Advanced Configuration

<details>
<summary><b>[+] Increasing GitHub API Rate Limit</b></summary>

If you set `fetchGithubData: true` for many projects, you may hit the unauthenticated GitHub API rate limit (60 requests/hour). To avoid this, create a **personal access token** (classic) with no extra scopes, and set it as an environment variable during the build:

1. Generate a token at [GitHub Settings > Tokens](https://github.com/settings/tokens).
2. In your repository, go to **Settings > Secrets and variables > Actions**.
3. Add a new secret named `GITHUB_TOKEN` (or any name) with the token value.
4. Update `.github/workflows/deploy.yml` to pass the token:

```yaml
- name: Build Astro site
  run: npm run build
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

5. Modify `src/utils/github.ts` to include the token in the request headers:

```typescript
const headers: HeadersInit = {};
if (import.meta.env.GITHUB_TOKEN) {
  headers.Authorization = `Bearer ${import.meta.env.GITHUB_TOKEN}`;
}
const response = await fetch(`https://api.github.com/repos/${owner}/${repo}`, { headers });
```

This increases your limit to 5,000 requests per hour.

</details>

<details>
<summary><b>[+] Using a Different Package Manager</b></summary>

The project is configured for `npm` by default. To use `pnpm` or `yarn`:

1. Delete `package-lock.json`.
2. Run `pnpm install` or `yarn install`.
3. Update the `cache` field in `.github/workflows/deploy.yml`:

```yaml
- name: Setup Node.js
  uses: actions/setup-node@v4
  with:
    node-version: 20
    cache: 'pnpm'   # or 'yarn'
```

</details>

---

### [>] Troubleshooting

<details>
<summary><b>[+] Common Issues & Fixes</b></summary>

| Symptom                                    | Likely Cause & Solution                                                                                   |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `npm install` fails                        | Ensure you are using Node.js v18+. Run `node -v`. Upgrade if necessary.                                    |
| Development server doesn't start           | Check for port conflicts. Use `npm run dev -- --port 3000` to specify a different port.                    |
| Project images not showing                 | Verify the image path in the Markdown frontmatter starts with `/images/`.                                  |
| GitHub stats not appearing                 | Ensure `fetchGithubData: true` and the repository URL is correct. Rate limit may be exceeded; try adding a token. |
| Deployment fails on GitHub Actions         | Check the workflow run logs. Common errors: incorrect `base` in `astro.config.mjs` or missing permissions. |
| Site displays incorrectly on custom domain | Update `astro.config.mjs` with `site: 'https://yourdomain.com'`. Also ensure the CNAME file exists in `public/`. |

</details>

---

### [>] Contributing

This is a personal portfolio template, but contributions to improve its flexibility or documentation are welcome.

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing-improvement`).
3. Commit your changes (`git commit -m 'Add some amazing improvement'`).
4. Push to the branch (`git push origin feature/amazing-improvement`).
5. Open a Pull Request.

---

### [>] License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it for your own portfolio.

---

### [>] Acknowledgements

- Built with [Astro](https://astro.build) — the web framework for content‑driven websites.
- Styled using [Tailwind CSS](https://tailwindcss.com).
- Deployed on [GitHub Pages](https://pages.github.com).
- Inspired by terminal aesthetics and modern MLOps dashboards.

---

<div align="center">
  <sub>[+] Crafted with [ ] and [x] by Khushal Pareta | <a href="https://kennny7.github.io">View Live</a></sub>
</div>
