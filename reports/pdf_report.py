from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)


def generate_pdf_report(
    filename,
    result,
    quality,
    ai_summary,
    ai_suggestions,
    improved_code,
    performance_score,
    overall_score
):

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleCustom",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=24,
        spaceAfter=8
    )

    subtitle_style = ParagraphStyle(
        "SubtitleCustom",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=12,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "HeadingCustom",
        parent=styles["Heading2"],
        fontSize=16,
        spaceBefore=12,
        spaceAfter=8
    )

    normal_style = ParagraphStyle(
        "NormalCustom",
        parent=styles["Normal"],
        fontSize=10,
        leading=14
    )

    code_style = ParagraphStyle(
        "CodeCustom",
        parent=styles["Code"],
        fontSize=8,
        leading=10
    )

    story = []

    # ==================================================
    # TITLE
    # ==================================================

    story.append(
        Paragraph(
            "🔍 ALGOLENS",
            title_style
        )
    )

    story.append(
        Paragraph(
            "AI Driven Code Performance Analyzer",
            subtitle_style
        )
    )

    story.append(
        Paragraph(
            "ANALYSIS REPORT",
            heading_style
        )
    )

    story.append(Spacer(1, 8))

    # ==================================================
    # SCORE TABLE
    # ==================================================

    score_data = [
        [
            "Overall Score",
            "Quality Score",
            "Performance Score"
        ],
        [
            f"{overall_score}/100",
            f"{quality['score']}/100",
            f"{performance_score}/100"
        ]
    ]

    score_table = Table(
        score_data,
        colWidths=[
            55 * mm,
            55 * mm,
            55 * mm
        ]
    )

    score_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.grey),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (-1, 1), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 11),
            ("TOPPADDING", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ])
    )

    story.append(score_table)

    story.append(Spacer(1, 15))

    # ==================================================
    # CODE METRICS
    # ==================================================

    story.append(
        Paragraph(
            "1. Code Metrics",
            heading_style
        )
    )

    metrics_data = [
        ["Metric", "Value"],
        ["Lines of Code", str(result["lines"])],
        ["Functions", str(result["functions"])],
        ["Loops", str(result["loops"])],
        ["Conditions", str(result["conditions"])],
        ["Variables", str(result["variables"])],
    ]

    metrics_table = Table(
        metrics_data,
        colWidths=[90 * mm, 60 * mm]
    )

    metrics_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.grey),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ALIGN", (1, 1), (1, -1), "CENTER"),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ])
    )

    story.append(metrics_table)

    # ==================================================
    # PERFORMANCE
    # ==================================================

    story.append(
        Paragraph(
            "2. Performance Analysis",
            heading_style
        )
    )

    performance_data = [
        ["Metric", "Result"],
        ["Time Complexity", str(result["time_complexity"])],
        ["Space Complexity", str(result["space_complexity"])],
        ["Maximum Loop Depth", str(result["loop_depth"])],
        ["Performance Score", f"{performance_score}/100"],
    ]

    performance_table = Table(
        performance_data,
        colWidths=[90 * mm, 60 * mm]
    )

    performance_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.grey),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ALIGN", (1, 1), (1, -1), "CENTER"),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ])
    )

    story.append(performance_table)

    # ==================================================
    # QUALITY
    # ==================================================

    story.append(
        Paragraph(
            "3. Code Quality",
            heading_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Quality Score:</b> {quality['score']}/100",
            normal_style
        )
    )

    story.append(Spacer(1, 6))

    if quality["issues"]:

        for issue in quality["issues"]:

            story.append(
                Paragraph(
                    f"• {issue}",
                    normal_style
                )
            )

    else:

        story.append(
            Paragraph(
                "✓ No major code quality issues detected.",
                normal_style
            )
        )

    # ==================================================
    # PERFORMANCE ISSUES
    # ==================================================

    story.append(
        Paragraph(
            "4. Performance Issues",
            heading_style
        )
    )

    if result["issues"]:

        for issue in result["issues"]:

            story.append(
                Paragraph(
                    f"• {issue}",
                    normal_style
                )
            )

    else:

        story.append(
            Paragraph(
                "✓ No major performance issues detected.",
                normal_style
            )
        )

    # ==================================================
    # AI SUMMARY
    # ==================================================

    story.append(
        Paragraph(
            "5. AI Code Summary",
            heading_style
        )
    )

    story.append(
        Paragraph(
            str(ai_summary).replace("\n", "<br/>"),
            normal_style
        )
    )

    # ==================================================
    # AI SUGGESTIONS
    # ==================================================

    story.append(
        Paragraph(
            "6. AI Improvement Suggestions",
            heading_style
        )
    )

    story.append(
        Paragraph(
            str(ai_suggestions).replace("\n", "<br/>"),
            normal_style
        )
    )

    # ==================================================
    # IMPROVED CODE
    # ==================================================

    story.append(
        Paragraph(
            "7. AI Improved Code",
            heading_style
        )
    )

    code_text = (
        str(improved_code)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br/>")
        .replace(" ", "&nbsp;")
    )

    story.append(
        Paragraph(
            code_text,
            code_style
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Generated by Algolens — AI Driven Code Performance Analyzer",
            subtitle_style
        )
    )

    # ==================================================
    # BUILD PDF
    # ==================================================

    doc.build(story)

    return filename