# CLAUDE.md — Make Money Websites

This repo tracks Dann Lopez's freelance strategy, gig guides, and client work documentation.

---

## Business Template

All client website commissions (Fiverr and direct) are built from this template:

**Repo:** https://github.com/Danncode10/business-template

### What the Template Includes

| Layer | Features |
|---|---|
| Landing Page | Hero, About, Services, Pricing, Testimonials, FAQ, Contact Form |
| SEO | Per-page meta title/description/OG image, sitemap, robots.txt |
| Blog | Full CMS with SEO controls per post, publish/schedule |
| Admin Dashboard | Site editor, lead inbox, blog CMS, media library, site settings |
| Auth | Login, signup, forgot/reset password, profile & security settings |
| Team | Roles management, audit log, analytics embed |
| Deployment | Vercel (frontend) + Supabase (database + auth) |

**Stack:** Next.js 15, Supabase (RLS), Tailwind CSS, TypeScript, Shadcn UI, TanStack Query

### How Client Projects Are Built

1. Clone the template repo
2. Configure Supabase project for the client (new project, new keys)
3. Fill in client content (branding, colors, logo, services, copy)
4. Deploy to Vercel under client's domain
5. Hand off admin credentials

### Where Client Projects Live

Clone each commission into:
```
~/Desktop/Clients/<ClientName>/
```

---

## Fiverr Gig Tiers (Gig 1: Business Websites)

| Tier | What's Included | Price | Delivery |
|---|---|---|---|
| Basic | Clean professional UI landing page + deployment | $80 | 3 days |
| Standard | Landing page + full SEO setup (meta, sitemap, OG, robots.txt) + deployment | $150 | 7 days |
| Premium | Landing page + SEO + management system + Blog (content SEO) + admin dashboard | $250 | 14 days |

---

## Key Files

- `FIVERR/fiverr-gig-guide.md` — Full gig setup reference
- `work-history.md` — Full work history for profile/proposals
- `my-charges.md` — Rate card
- `UPSKILL/upwork-connects-guide.md` — Upwork strategy notes
