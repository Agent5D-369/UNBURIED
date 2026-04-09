# UNBURIED static site

A mobile-first GitHub Pages site for a filmmaker-first distribution network.

## Files
- `index.html` – main landing page
- `filmmakers.html` – filmmaker / rights-holder page
- `hosts.html` – local screening and host page
- `investors.html` – investor thesis page
- `styles.css` – shared styles
- `script.js` – mobile nav only
- `assets/placeholders/` – placeholder SVG art blocks
- `canva-prompts.txt` – image generation prompts mapped to each placeholder
- `robots.txt`, `sitemap.xml`, `llms.txt`, `llms-full.txt`, `site.webmanifest`

## Before launch
1. Replace `https://YOURDOMAIN.com` in:
   - `index.html`
   - `filmmakers.html`
   - `hosts.html`
   - `investors.html`
   - `sitemap.xml`
   - `llms.txt`
   - `llms-full.txt`
2. Replace Formspree placeholders:
   - `YOUR_WAITLIST_FORM_ID`
   - `YOUR_FILMMAKER_FORM_ID`
   - `YOUR_INVESTOR_FORM_ID`
3. Swap placeholder SVGs with final images.
4. Verify trademark and domain availability for the working brand name `UNBURIED`.

## GitHub Pages
Push the files to a public repo and enable GitHub Pages from the root. GitHub Pages can serve static HTML, CSS, and JS directly from a repository.

## Notes
- Built with semantic HTML for strong crawlability.
- Mobile-first layout.
- Includes canonical tags, OG tags, FAQ schema, sitemap, robots, and llms files.
- No build step required.
