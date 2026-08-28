import sys
import os

# ==================================================
# PROJECT ROOT
# ==================================================

PROJECT_ROOT = os.path.dirname(
    os.path.abspath(__file__)
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


# ==================================================
# IMPORTS
# ==================================================

import streamlit as st

from ml.ml_predictor import predict_quality

from analyzer.code_parser import analyze_code
from analyzer.quality import analyze_quality

from ai.ai_analyzer import (
    summarize_code,
    suggest_improvements,
    generate_improved_code
)

from reports.report_generator import generate_report
from reports.pdf_report import generate_pdf_report


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Algolens",
    page_icon="🔍",
    layout="wide"
)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("🔍 Algolens")

    st.write(
        "AI Driven Code Performance Analyzer"
    )

    st.divider()

    st.subheader("📌 Features")

    st.write("📊 Code Metrics")
    st.write("⚡ Performance Analysis")
    st.write("🏆 Code Quality")
    st.write("🤖 AI Code Summary")
    st.write("💡 AI Suggestions")
    st.write("✨ AI Code Optimization")
    st.write("🤖 ML Quality Prediction")
    st.write("📄 Analysis Report")
    st.write("📑 PDF Report")

    st.divider()

    st.subheader("🛠️ Technology")

    st.write("🐍 Python")
    st.write("🎨 Streamlit")
    st.write("🤖 Google Gemini AI")
    st.write("🌲 Random Forest ML")
    st.write("📄 ReportLab")

    st.divider()

    st.subheader("📋 Project")

    st.write("AI-powered code analysis")
    st.write("Performance optimization")
    st.write("Code quality evaluation")
    st.write("ML-based quality prediction")
    st.write("Automated analysis reports")

    st.divider()

    st.caption("Algolens v1.0")
    st.caption("AI-powered code analysis")


# ==================================================
# HEADER
# ==================================================

st.title("🔍 Algolens")

st.subheader(
    "AI Driven Code Performance Analyzer"
)

st.write(
    "Analyze your code, understand its performance, "
    "evaluate code quality, and get AI-powered "
    "summaries, suggestions, optimizations, "
    "ML-based quality prediction, and detailed "
    "analysis reports."
)

st.divider()


# ==================================================
# CODE INPUT
# ==================================================

st.subheader("📝 Code Input")

language = st.selectbox(
    "Select Programming Language",
    ["Python"]
)

code = st.text_area(
    "Paste your code below:",
    height=300,
    placeholder="Paste your Python code here..."
)


# ==================================================
# ANALYZE BUTTON
# ==================================================

if st.button(
    "🚀 Analyze Code",
    type="primary"
):

    if not code.strip():

        st.warning(
            "⚠️ Please enter some code first."
        )

    else:

        # ==================================================
        # STATIC ANALYSIS
        # ==================================================

        with st.spinner(
            "🔍 Analyzing your code..."
        ):

            result = analyze_code(code)
            quality = analyze_quality(code)

        if result is None or quality is None:

            st.error(
                "❌ Invalid Python code. "
                "Please check your syntax."
            )

        else:

            st.success(
                "✅ Code analyzed successfully!"
            )


            # ==================================================
            # QUALITY SCORE
            # ==================================================

            quality_score = quality["score"]


            # ==================================================
            # ML QUALITY SCORE
            # ==================================================

            try:

                ml_quality_score = predict_quality(
                    code
                )

            except Exception as e:

                ml_quality_score = None

                st.warning(
                    "⚠️ ML quality prediction "
                    "could not be generated."
                )

                st.caption(
                    f"ML Error: {str(e)}"
                )


            # ==================================================
            # PERFORMANCE SCORE
            # ==================================================

            performance_score = 100

            if result["loop_depth"] >= 2:

                performance_score -= 10

            if result["loop_depth"] >= 3:

                performance_score -= 10

            performance_score -= min(
                len(result["issues"]) * 5,
                30
            )

            performance_score = max(
                0,
                min(100, performance_score)
            )


            # ==================================================
            # OVERALL SCORE
            # ==================================================

            overall_score = int(
                (quality_score * 0.6)
                + (performance_score * 0.4)
            )

            overall_score = max(
                0,
                min(100, overall_score)
            )


            # ==================================================
            # DASHBOARD
            # ==================================================

            st.divider()

            st.subheader(
                "📊 Analysis Dashboard"
            )

            score_col, metric_col1, metric_col2, metric_col3, ml_col = st.columns(5)

            with score_col:

                st.metric(
                    "Overall Score",
                    f"{overall_score}/100"
                )

            with metric_col1:

                st.metric(
                    "Lines",
                    result["lines"]
                )

            with metric_col2:

                st.metric(
                    "Functions",
                    result["functions"]
                )

            with metric_col3:

                st.metric(
                    "Quality",
                    f"{quality_score}/100"
                )

            with ml_col:

                if ml_quality_score is not None:

                    st.metric(
                        "ML Quality",
                        f"{ml_quality_score}/100"
                    )

                else:

                    st.metric(
                        "ML Quality",
                        "N/A"
                    )

            st.progress(
                overall_score / 100
            )


            # ==================================================
            # TABS
            # ==================================================

            overview_tab, performance_tab, ai_tab = st.tabs(
                [
                    "📊 Overview",
                    "⚡ Performance",
                    "🤖 AI Insights"
                ]
            )


            # ==================================================
            # OVERVIEW TAB
            # ==================================================

            with overview_tab:

                st.subheader(
                    "📊 Code Overview"
                )

                col1, col2, col3, col4 = st.columns(4)

                with col1:

                    st.metric(
                        "Lines of Code",
                        result["lines"]
                    )

                with col2:

                    st.metric(
                        "Functions",
                        result["functions"]
                    )

                with col3:

                    st.metric(
                        "Loops",
                        result["loops"]
                    )

                with col4:

                    st.metric(
                        "Conditions",
                        result["conditions"]
                    )


                st.divider()


                # ---------------- QUALITY ----------------

                st.subheader(
                    "🏆 Code Quality"
                )

                quality_col1, quality_col2 = st.columns(
                    [1, 2]
                )

                with quality_col1:

                    st.metric(
                        "Quality Score",
                        f"{quality_score}/100"
                    )

                with quality_col2:

                    st.progress(
                        quality_score / 100
                    )


                st.divider()


                # ---------------- ML QUALITY ----------------

                st.subheader(
                    "🤖 ML-Based Code Quality Prediction"
                )

                if ml_quality_score is not None:

                    ml_col1, ml_col2 = st.columns(
                        [1, 2]
                    )

                    with ml_col1:

                        st.metric(
                            "Predicted Quality Score",
                            f"{ml_quality_score}/100"
                        )

                    with ml_col2:

                        st.progress(
                            ml_quality_score / 100
                        )

                    st.caption(
                        "Score predicted using the trained "
                        "Random Forest ML model."
                    )

                else:

                    st.warning(
                        "ML quality prediction unavailable."
                    )


                st.divider()


                # ---------------- QUALITY ISSUES ----------------

                st.subheader(
                    "🔎 Code Quality Issues"
                )

                if quality["issues"]:

                    for issue in quality["issues"]:

                        st.warning(issue)

                else:

                    st.success(
                        "✅ No major code quality issues detected."
                    )


                st.divider()


                # ---------------- STATIC SUGGESTIONS ----------------

                st.subheader(
                    "🛠️ Static Analyzer Suggestions"
                )

                if quality["suggestions"]:

                    for suggestion in quality["suggestions"]:

                        st.info(suggestion)

                else:

                    st.success(
                        "✅ No major suggestions."
                    )


                st.divider()


                # ---------------- DETAILS ----------------

                st.subheader(
                    "📋 Additional Details"
                )

                detail_col1, detail_col2, detail_col3 = st.columns(3)

                with detail_col1:

                    st.write(
                        f"**Variables:** "
                        f"{result['variables']}"
                    )

                with detail_col2:

                    st.write(
                        f"**Total Loops:** "
                        f"{result['loops']}"
                    )

                with detail_col3:

                    st.write(
                        f"**Total Conditions:** "
                        f"{result['conditions']}"
                    )


            # ==================================================
            # PERFORMANCE TAB
            # ==================================================

            with performance_tab:

                st.subheader(
                    "⚡ Performance Analysis"
                )

                perf_col1, perf_col2, perf_col3 = st.columns(3)

                with perf_col1:

                    st.metric(
                        "Time Complexity",
                        result["time_complexity"]
                    )

                with perf_col2:

                    st.metric(
                        "Space Complexity",
                        result["space_complexity"]
                    )

                with perf_col3:

                    st.metric(
                        "Loop Depth",
                        result["loop_depth"]
                    )


                st.divider()


                # ---------------- PERFORMANCE SCORE ----------------

                st.subheader(
                    "📈 Performance Score"
                )

                st.metric(
                    "Performance Score",
                    f"{performance_score}/100"
                )

                st.progress(
                    performance_score / 100
                )


                st.divider()


                # ---------------- PERFORMANCE ISSUES ----------------

                st.subheader(
                    "⚠️ Performance Issues"
                )

                if result["issues"]:

                    for issue in result["issues"]:

                        st.warning(issue)

                else:

                    st.success(
                        "✅ No major performance issues detected."
                    )


                st.divider()


                # ---------------- PERFORMANCE SUMMARY ----------------

                st.subheader(
                    "📋 Performance Summary"
                )

                st.write(
                    f"**Time Complexity:** "
                    f"{result['time_complexity']}"
                )

                st.write(
                    f"**Space Complexity:** "
                    f"{result['space_complexity']}"
                )

                st.write(
                    f"**Maximum Loop Depth:** "
                    f"{result['loop_depth']}"
                )


            # ==================================================
            # AI TAB
            # ==================================================

            with ai_tab:

                st.subheader(
                    "🤖 AI Code Analysis"
                )


                # ==================================================
                # AI SUMMARY
                # ==================================================

                st.markdown(
                    "### 🤖 Code Summary"
                )

                try:

                    with st.spinner(
                        "Gemini is analyzing your code..."
                    ):

                        ai_summary = summarize_code(
                            code
                        )

                    st.markdown(
                        ai_summary
                    )

                except Exception as e:

                    ai_summary = (
                        "AI summary could not be generated."
                    )

                    st.error(
                        ai_summary
                    )

                    st.caption(
                        f"Error: {str(e)}"
                    )


                st.divider()


                # ==================================================
                # AI SUGGESTIONS
                # ==================================================

                st.markdown(
                    "### 💡 Improvement Suggestions"
                )

                try:

                    with st.spinner(
                        "Gemini is generating suggestions..."
                    ):

                        ai_suggestions = suggest_improvements(
                            code
                        )

                    st.markdown(
                        ai_suggestions
                    )

                except Exception as e:

                    ai_suggestions = (
                        "AI suggestions could not be generated."
                    )

                    st.error(
                        ai_suggestions
                    )

                    st.caption(
                        f"Error: {str(e)}"
                    )


                st.divider()


                # ==================================================
                # AI IMPROVED CODE
                # ==================================================

                st.markdown(
                    "### ✨ AI Improved Code"
                )

                try:

                    with st.spinner(
                        "Gemini is generating improved code..."
                    ):

                        improved_code = generate_improved_code(
                            code
                        )

                    st.code(
                        improved_code,
                        language="python"
                    )

                except Exception as e:

                    improved_code = (
                        "Improved code could not be generated."
                    )

                    st.error(
                        improved_code
                    )

                    st.caption(
                        f"Error: {str(e)}"
                    )


            # ==================================================
            # TEXT ANALYSIS REPORT
            # ==================================================

            st.divider()

            st.subheader(
                "📄 Analysis Report"
            )

            try:

                report = generate_report(
                    result=result,
                    quality=quality,
                    ai_summary=ai_summary,
                    ai_suggestions=ai_suggestions,
                    performance_score=performance_score,
                    overall_score=overall_score
                )

                st.success(
                    "✅ Analysis report generated successfully!"
                )

                with st.expander(
                    "👁️ Preview Text Report"
                ):

                    st.text(report)

                st.download_button(
                    label="📥 Download Text Report",
                    data=report,
                    file_name="algolens_analysis_report.txt",
                    mime="text/plain"
                )

            except Exception as e:

                st.error(
                    "❌ Text report could not be generated."
                )

                st.caption(
                    f"Error: {str(e)}"
                )


            # ==================================================
            # PDF REPORT
            # ==================================================

            st.divider()

            st.subheader(
                "📑 Professional PDF Report"
            )

            try:

                pdf_path = "algolens_analysis_report.pdf"

                generate_pdf_report(
                    filename=pdf_path,
                    result=result,
                    quality=quality,
                    ai_summary=ai_summary,
                    ai_suggestions=ai_suggestions,
                    improved_code=improved_code,
                    performance_score=performance_score,
                    overall_score=overall_score
                )

                st.success(
                    "✅ Professional PDF report generated!"
                )

                with open(
                    pdf_path,
                    "rb"
                ) as pdf_file:

                    st.download_button(
                        label="📥 Download PDF Report",
                        data=pdf_file,
                        file_name="algolens_analysis_report.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:

                st.error(
                    "❌ PDF report could not be generated."
                )

                st.caption(
                    f"Error: {str(e)}"
                )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "Algolens — AI Driven Code Performance Analyzer | v1.0"
)