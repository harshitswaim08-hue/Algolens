def generate_report(
    result,
    quality,
    ai_summary,
    ai_suggestions,
    performance_score,
    overall_score
):
    """
    Generate a complete Algolens analysis report.
    """

    report = f"""
==================================================
                ALGOLENS
       AI DRIVEN CODE PERFORMANCE ANALYZER
==================================================

                    ANALYSIS REPORT
--------------------------------------------------

1. CODE METRICS
--------------------------------------------------

Lines of Code       : {result["lines"]}
Functions           : {result["functions"]}
Loops               : {result["loops"]}
Conditions          : {result["conditions"]}
Variables           : {result["variables"]}


2. PERFORMANCE ANALYSIS
--------------------------------------------------

Time Complexity     : {result["time_complexity"]}
Space Complexity    : {result["space_complexity"]}
Maximum Loop Depth  : {result["loop_depth"]}

Performance Score   : {performance_score}/100


3. CODE QUALITY
--------------------------------------------------

Quality Score       : {quality["score"]}/100
Overall Score       : {overall_score}/100


4. PERFORMANCE ISSUES
--------------------------------------------------
"""

    if result["issues"]:

        for issue in result["issues"]:
            report += f"- {issue}\n"

    else:

        report += "- No major performance issues detected.\n"


    report += """
    
5. CODE QUALITY ISSUES
--------------------------------------------------
"""

    if quality["issues"]:

        for issue in quality["issues"]:
            report += f"- {issue}\n"

    else:

        report += "- No major code quality issues detected.\n"


    report += f"""

6. AI CODE SUMMARY
--------------------------------------------------

{ai_summary}


7. AI IMPROVEMENT SUGGESTIONS
--------------------------------------------------

{ai_suggestions}


==================================================
              END OF ANALYSIS REPORT
==================================================
"""

    return report