"""
Builds a branded one-page PDF case study / sell-sheet for Dann Lopez's Fiverr gig,
showcasing AttyJuan.ai (AI-powered legal SaaS platform).
Same dark charcoal + red brand look as his other case-study sell-sheet.
"""

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

# ---- Brand palette (same as Chris Auto Shine sell-sheet) ----
CHARCOAL = HexColor("#161616")
CHARCOAL_LIGHT = HexColor("#222222")
RED = HexColor("#E0252B")
WHITE = HexColor("#F5F5F5")
GRAY = HexColor("#B0B0B0")
LIGHT_GRAY = HexColor("#D8D8D8")

PAGE_W, PAGE_H = LETTER
MARGIN = 0.65 * inch

OUTPUT_PATH = "/Users/lesterdannlopez/Desktop/Make Money Websites/FIVERR/Documents/Dann-Lopez-Case-Study-AttyJuan-AI.pdf"


def draw_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(CHARCOAL)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(RED)
    canvas.rect(0, PAGE_H - 0.12 * inch, PAGE_W, 0.12 * inch, fill=1, stroke=0)
    canvas.setFillColor(RED)
    canvas.rect(0, 0, PAGE_W, 0.06 * inch, fill=1, stroke=0)
    canvas.setFillColor(GRAY)
    canvas.setFont("Helvetica", 8.5)
    canvas.drawString(MARGIN, 0.32 * inch, "Dann Lopez  •  Full-Stack & AI Developer  •  Fiverr: dannbuilds  •  Lesterdannlopez7@gmail.com")
    canvas.drawRightString(PAGE_W - MARGIN, 0.32 * inch, "Portfolio: dannlopez.vercel.app")
    canvas.restoreState()


# ---- Styles ----
styles = getSampleStyleSheet()

label_style = ParagraphStyle(
    "Label", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10.5,
    textColor=RED, spaceAfter=2, leading=13,
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
    "SectionHeading", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=11.5,
    textColor=RED, spaceBefore=8, spaceAfter=3, leading=13,
)
body_style = ParagraphStyle(
    "Body", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5,
    textColor=LIGHT_GRAY, leading=13.5, spaceAfter=2,
)
bullet_style = ParagraphStyle(
    "Bullet", parent=body_style, leftIndent=14, bulletIndent=2, spaceAfter=1.5, leading=13,
)
tech_style = ParagraphStyle(
    "Tech", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10,
    textColor=WHITE, leading=14,
)
quote_style = ParagraphStyle(
    "Quote", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=12.5,
    textColor=WHITE, leading=17,
)
cta_heading_style = ParagraphStyle(
    "CTAHeading", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=12.5,
    textColor=WHITE, spaceBefore=2, spaceAfter=3,
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
        topMargin=0.5 * inch, bottomMargin=0.5 * inch,
        title="Case Study — AttyJuan.ai | Dann Lopez",
        author="Dann Lopez",
    )
    frame = Frame(MARGIN, 0.5 * inch, PAGE_W - 2 * MARGIN, PAGE_H - 1.15 * inch, id="main")
    doc.addPageTemplates([PageTemplate(id="branded", frames=[frame], onPage=draw_background)])

    story = []

    # Header
    story.append(Paragraph("CASE STUDY", label_style))
    story.append(Paragraph("AttyJuan.ai", title_style))
    story.append(Paragraph("AI-Powered Legal SaaS Platform — Co-Founded &amp; Engineered", subtitle_style))
    story.append(Spacer(1, 5))
    story.append(HRFlowable(width="100%", thickness=1.1, color=RED, spaceAfter=7))

    # The Project
    story.append(Paragraph("THE PROJECT", heading_style))
    story.append(Paragraph(
        "AttyJuan.ai — a multi-tenant case-management platform built specifically for Filipino "
        "solo lawyers and small law firms. Think &ldquo;Google Calendar meets Notion meets an AI "
        "legal assistant,&rdquo; purpose-built for the Philippine legal context.", body_style))

    # The Problem
    story.append(Paragraph("THE PROBLEM", heading_style))
    story.append(Paragraph(
        "Philippine lawyers run their practice on physical folders, spreadsheets, WhatsApp groups, "
        "and memory. Every major legal tool (Clio, MyCase, PracticePanther) is built for the US "
        "market — wrong pricing, wrong compliance, wrong workflows. Lawyers miss hearings, lose "
        "documents, and burn hours on admin instead of legal work.", body_style))

    # What I Built
    story.append(Paragraph("WHAT I BUILT", heading_style))
    story.extend(bullets([
        "Multi-tenant SaaS architecture with strict Row-Level Security (RLS) — every firm's data fully isolated",
        "Full case management — client records, court details, status tracking, case timelines",
        "AI document pipeline: upload a PDF/Word file, GPT-4o Mini returns a structured summary (parties, issues, key dates)",
        "Context-aware AI assistant answering natural-language questions using only the lawyer's own data",
        "Calendar &amp; scheduling system with conflict detection and automated email reminders",
        "Tiered subscription billing wired to PayMongo (GCash/Maya) and Stripe webhooks",
    ]))

    # Tech stack
    story.append(Paragraph("TECH STACK", heading_style))
    story.append(Paragraph(
        "Next.js 15 &nbsp;•&nbsp; Supabase (PostgreSQL + RLS) &nbsp;•&nbsp; Tailwind CSS v4 &nbsp;•&nbsp; "
        "OpenAI GPT-4o Mini &nbsp;•&nbsp; TanStack Query &nbsp;•&nbsp; PayMongo &nbsp;•&nbsp; Stripe",
        tech_style))

    # The Result
    story.append(Paragraph("THE RESULT", heading_style))
    story.extend(bullets([
        "A production-grade, multi-tenant SaaS platform — architected and engineered solo as co-founder",
        "AI features that turn hours of document review into minutes",
        "First purpose-built case-management tool for the Philippine legal market",
    ]))

    story.append(Spacer(1, 5))

    # Pull-quote block
    quote_table = Table(
        [[Paragraph(
            "&ldquo;I don&rsquo;t just build websites — I build systems that run businesses.&rdquo;<br/>"
            '<font color="#B0B0B0" size="9.5">— Dann Lopez, Full-Stack &amp; AI Developer</font>',
            quote_style)]],
        colWidths=[PAGE_W - 2 * MARGIN],
    )
    quote_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CHARCOAL_LIGHT),
        ("LINEBEFORE", (0, 0), (0, -1), 4, RED),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(quote_table)
    story.append(Spacer(1, 6))

    # What this means for you
    story.append(Paragraph("WHAT THIS MEANS FOR YOUR BUSINESS", heading_style))
    story.append(Paragraph(
        "This is the same engineering approach I bring to every project — secure multi-tenant "
        "architecture, AI integrations, real authentication &amp; payments, and dashboards that "
        "actually save people time. Booking systems, client portals, internal tools, or AI-powered "
        "features bolted onto your existing site — I build it production-grade from day one.", body_style))

    story.append(Spacer(1, 5))
    story.append(HRFlowable(width="100%", thickness=0.75, color=HexColor("#3a3a3a"), spaceAfter=7))

    # CTA
    story.append(Paragraph("Ready to start?", cta_heading_style))
    story.append(Paragraph(
        "Message me with what you&rsquo;re trying to build and I&rsquo;ll map it to the right package — "
        '<font color="#FFFFFF"><b>Basic</b></font> (landing page), '
        '<font color="#FFFFFF"><b>Standard</b></font> (+ full SEO), or '
        '<font color="#FFFFFF"><b>Premium</b></font> (+ management dashboard, blog, and custom features like the ones above).',
        body_style))

    doc.build(story)
    print(f"Saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    build()
