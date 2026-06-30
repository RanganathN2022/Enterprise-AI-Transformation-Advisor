from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


styles = getSampleStyleSheet()

title_style = styles["Title"]
title_style.fontName = "Arial"
title_style.alignment = TA_CENTER
heading_style = styles["Heading1"]
normal_style = styles["BodyText"]


def generate_pdf(
    company_name,
    industry,
    employees,
    revenue,
    readiness,
    maturity,
    roi_result,
    risk_result,
    roadmap,
    ai_report,
):
    """
    Generate Enterprise AI Transformation Report.
    Returns the generated PDF filename.
    """

    filename = "AI_Transformation_Report.pdf"

    doc = SimpleDocTemplate(
    filename,
    rightMargin=30,
    leftMargin=30,
    topMargin=30,
    bottomMargin=30
    )

    story = []
    pdfmetrics.registerFont(
    TTFont(
        "Arial",
        "C:/Windows/Fonts/arial.ttf"
    )
)
    # ------------------------
    # Cover Page
    # ------------------------

    story.append(
        Paragraph(
            "Enterprise AI Transformation Advisor",
            title_style,
        )
    )

    story.append(Spacer(1, 0.3 * inch))

    story.append(
        Paragraph(
            "<b>AI Strategy Assessment Report</b>",
            heading_style,
        )
    )

    story.append(Spacer(1, 0.5 * inch))

    cover = [
        ["Company", company_name],
        ["Industry", industry],
        ["Employees", str(employees)],
        ["Annual Revenue", f"INR {revenue:,} Crores"],
    ]

    table = Table(cover, colWidths=[2.2 * inch, 4 * inch])

    table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    story.append(table)

    story.append(Spacer(1, 2 * inch))

    story.append(Paragraph("<b>Prepared By</b>", heading_style))
    story.append(Paragraph("Ranganath N", normal_style))
    story.append(
        Paragraph(
            "Enterprise AI Transformation Advisor v1.0",
            normal_style,
        )
    )

    story.append(PageBreak())

    # ------------------------
    # Executive Summary
    # ------------------------

    story.append(Paragraph("Executive Summary", heading_style))
    story.append(Spacer(1, 0.2 * inch))

    summary = [
        ["AI Readiness", f"{readiness}/100"],
        ["Estimated ROI", f"{roi_result['roi']}%"],
        ["Risk Level", risk_result["risk"]],
    ]

    t = Table(summary, colWidths=[2.5 * inch, 3 * inch])

    t.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#EAF2F8")),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    story.append(t)

    story.append(PageBreak())

    # ------------------------
    # AI Maturity
    # ------------------------

    story.append(Paragraph("AI Maturity Assessment", heading_style))
    story.append(Spacer(1, 0.2 * inch))

    maturity_rows = [["Category", "Score"]]

    for k, v in maturity.items():
        maturity_rows.append([k, f"{v}%"])

    mt = Table(maturity_rows, colWidths=[3.5 * inch, 2 * inch])

    mt.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D6EAF8")),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    story.append(mt)

    story.append(PageBreak())

    # ------------------------
    # ROI
    # ------------------------

    story.append(Paragraph("ROI Analysis", heading_style))

    roi_rows = [
        ["Implementation Cost", f"INR {roi_result['cost']:,}"],
        ["Annual Savings", f"INR {roi_result['savings']:,}"],
        ["Estimated ROI", f"{roi_result['roi']}%"],
    ]

    rt = Table(roi_rows, colWidths=[3.5 * inch, 2.5 * inch])

    rt.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#FCF3CF")),
            ]
        )
    )

    story.append(rt)

    story.append(PageBreak())

    # ------------------------
    # Responsible AI
    # ------------------------

    story.append(Paragraph("Responsible AI Assessment", heading_style))

    risk_rows = [
        ["Risk Level", risk_result["risk"]],
        ["Privacy", risk_result["privacy"]],
        ["Explainability", risk_result["explainability"]],
    ]

    risk_table = Table(risk_rows, colWidths=[3.5 * inch, 2.5 * inch])

    risk_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#FADBD8")),
            ]
        )
    )

    story.append(risk_table)

    story.append(PageBreak())

    # ------------------------
    # Roadmap
    # ------------------------

    story.append(Paragraph("AI Transformation Roadmap", heading_style))

    for step in roadmap:
        story.append(Paragraph("- " + step, normal_style))

    story.append(PageBreak())

  # ------------------------
# Gemini Report
# ------------------------

    story.append(Paragraph("AI Strategy Recommendations", heading_style))
    story.append(Spacer(1, 0.2 * inch))

    lines = ai_report.split("\n")

    for line in lines:

        line = line.strip()

        # Empty line
        if line == "":
            story.append(Spacer(1, 0.12 * inch))
            continue

        # Main Heading
        if line.isupper():
            story.append(
                Paragraph(
                    f"<b><font size=16>{line}</font></b>",
                    heading_style
                )
            )
            story.append(Spacer(1, 0.1 * inch))
            continue

        # Bullet Point
        if line.startswith("•"):
            story.append(
                Paragraph(
                    "&bull; " + line[1:].strip(),
                    normal_style
                )
            )
            continue

        # Numbered Point
        if line.startswith(("1.", "2.", "3.", "4.", "5.")):
            story.append(
                Paragraph(
                    f"<b>{line}</b>",
                    normal_style
                )
            )
            continue

        # Normal Paragraph
        story.append(
            Paragraph(
                line,
                normal_style
            )
        )

    doc.build(story)

    return filename