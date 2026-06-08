"""
Builds a branded one-page PDF case study / sell-sheet for Dann Lopez's Fiverr gig.
Dark charcoal background + red accent, matching the "Chris Auto Shine Detailing"
brand look used in his gig gallery images.
"""

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

# ---- Brand palette ----
CHARCOAL = HexColor("#161616")
CHARCOAL_LIGHT = HexColor("#222222")
RED = HexColor("#E0252B")
WHITE = HexColor("#F5F5F5")
GRAY = HexColor("#B0B0B0")
LIGHT_GRAY = HexColor("#D8D8D8")

PAGE_W, PAGE_H = LETTER
MARGIN = 0.65 * inch

OUTPUT_PATH = "/Users/lesterdannlopez/Desktop/Make Money Websites/FIVERR/Documents/Dann-Lopez-Case-Study-Chris-Auto-Shine.pdf"


def draw_background(canvas, doc):
    canvas.saveState()
    # Full charcoal background
    canvas.setFillColor(CHARCOAL)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # Top red accent bar
    canvas.setFillColor(RED)
    canvas.rect(0, PAGE_H - 0.12 * inch, PAGE_W, 0.12 * inch, fill=1, stroke=0)
    # Bottom thin red rule
    canvas.setFillColor(RED)
    canvas.rect(0, 0, PAGE_W, 0.06 * inch, fill=1, stroke=0)
    # Footer text
    canvas.setFillColor(GRAY)
    canvas.setFont("Helvetica", 8.5)
    canvas.drawString(MARGIN, 0.32 * inch, "Dann Lopez  •  Full-Stack Developer  •  Fiverr: dannbuilds  •  Lesterdannlopez7@gmail.com")
    canvas.drawRightString(PAGE_W - MARGIN, 0.32 * inch, "Portfolio: dannlopez.vercel.app")
    canvas.restoreState()


# ---- Styles ----
styles = getSampleStyleSheet()

label_style = ParagraphStyle(
    "Label", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10.5,
    textColor=RED, spaceAfter=2, leading=13, tracking=1,
)
title_style = ParagraphStyle(
    "TitleBig", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=27,
    textColor=WHITE, leading=31, spaceAfter=4, alignment=TA_LEFT,
)
subtitle_style = ParagraphStyle(
    "Subtitle", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=12.5,
    textColor=GRAY, leading=16, spaceAfter=2,
)
heading_style = ParagraphStyle(
    "SectionHeading", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=12,
    textColor=RED, spaceBefore=10, spaceAfter=4, leading=14,
)
body_style = ParagraphStyle(
    "Body", parent=styles["Normal"], fontName="Helvetica", fontSize=10,
    textColor=LIGHT_GRAY, leading=15, spaceAfter=3,
)
bullet_style = ParagraphStyle(
    "Bullet", parent=body_style, leftIndent=14, bulletIndent=2, spaceAfter=2,
)
tech_style = ParagraphStyle(
    "Tech", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10.5,
    textColor=WHITE, leading=15,
)
quote_style = ParagraphStyle(
    "Quote", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=13,
    textColor=WHITE, leading=18,
)
quote_attr_style = ParagraphStyle(
    "QuoteAttr", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5,
    textColor=GRAY, leading=13, spaceBefore=4,
)
cta_heading_style = ParagraphStyle(
    "CTAHeading", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=13,
    textColor=WHITE, spaceBefore=2, spaceAfter=4,
)


def bullets(items):
    flow = []
    for item in items:
        flow.append(Paragraph(f'<font color="#E0252B">&#9656;</font>&nbsp;&nbsp;{item}', bullet_style))
    return flow


def build():
    doc = BaseDocTemplate(
        OUTPUT_PATH,
        pagesize=LETTER,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=0.55 * inch, bottomMargin=0.55 * inch,
        title="Case Study — Chris Auto Shine Detailing | Dann Lopez",
        author="Dann Lopez",
    )
    frame = Frame(MARGIN, 0.55 * inch, PAGE_W - 2 * MARGIN, PAGE_H - 1.25 * inch, id="main")
    doc.addPageTemplates([PageTemplate(id="branded", frames=[frame], onPage=draw_background)])

    story = []

    # Header
    story.append(Paragraph("CASE STUDY", label_style))
    story.append(Paragraph("Chris Auto Shine Detailing", title_style))
    story.append(Paragraph("Premium Business Website — Designed, Built &amp; Launched", subtitle_style))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.1, color=RED, spaceAfter=8))

    # The Client
    story.append(Paragraph("THE CLIENT", heading_style))
    story.append(Paragraph(
        "Chris Auto Shine Detailing — an Australian automotive detailing company that needed "
        "an online presence as premium as the cars they work on.", body_style))

    # The Challenge
    story.append(Paragraph("THE CHALLENGE", heading_style))
    story.append(Paragraph(
        "No website. No way for customers to browse services, see pricing, or get in touch online — "
        "and in a visual business like detailing, looking unpolished online means losing customers "
        "before they even call.", body_style))

    # What I Built
    story.append(Paragraph("WHAT I BUILT", heading_style))
    story.extend(bullets([
        "Fully responsive landing page — hero, services, pricing packages, testimonials, contact",
        "Dynamic, reusable pricing-package components and interactive service modals",
        "Mobile-first design tested across phones, tablets, and desktops",
        "Lightweight internal management system to track bookings and finances",
        "Optimized production build (Vite) for fast load times and instant navigation",
    ]))

    # Tech stack row
    story.append(Paragraph("TECH STACK", heading_style))
    story.append(Paragraph(
        "React &nbsp;•&nbsp; Tailwind CSS &nbsp;•&nbsp; Vite &nbsp;•&nbsp; JavaScript &nbsp;•&nbsp; PostCSS &nbsp;•&nbsp; ESLint",
        tech_style))

    # The Result
    story.append(Paragraph("THE RESULT", heading_style))
    story.extend(bullets([
        "Live, professional site: chrisautoshinedetailing.com.au",
        "Fast-loading, mobile-optimized customer experience",
        "A digital storefront that finally matches the premium quality of the business itself",
    ]))

    story.append(Spacer(1, 6))

    # Pull-quote block (table used as a bordered/colored box)
    quote_table = Table(
        [[Paragraph(
            "&ldquo;World-class work. Freelancer price.&rdquo;<br/>"
            '<font color="#B0B0B0" size="9.5">— Dann Lopez, Full-Stack Developer</font>',
            quote_style)]],
        colWidths=[PAGE_W - 2 * MARGIN],
    )
    quote_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CHARCOAL_LIGHT),
        ("LINEBEFORE", (0, 0), (0, -1), 4, RED),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    story.append(quote_table)
    story.append(Spacer(1, 8))

    # What this means for you
    story.append(Paragraph("WHAT THIS MEANS FOR YOUR BUSINESS", heading_style))
    story.append(Paragraph(
        "Whether you run a restaurant, salon, clinic, auto shop, or any local service business — "
        "I build the same standard of site for you: clean code, mobile-first design, fast load times, "
        "and a look that makes your business feel as trustworthy online as it is in person.", body_style))

    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=0.75, color=HexColor("#3a3a3a"), spaceAfter=8))

    # CTA
    story.append(Paragraph("Ready to start?", cta_heading_style))
    story.append(Paragraph(
        "Message me with a bit about your business and I&rsquo;ll recommend the right package — "
        '<font color="#FFFFFF"><b>Basic</b></font> (landing page), '
        '<font color="#FFFFFF"><b>Standard</b></font> (+ full SEO), or '
        '<font color="#FFFFFF"><b>Premium</b></font> (+ management dashboard &amp; blog).',
        body_style))

    doc.build(story)
    print(f"Saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    build()
