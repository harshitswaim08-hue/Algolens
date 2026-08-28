import streamlit as st

from analyzer.code_parser import analyze_code
from analyzer.quality import analyze_quality

from ai.ai_analyzer import (
    summarize_code,
    suggest_improvements,
    generate_improved_code
)


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Algolens",
    page_icon="🔍",
    layout="wide"
)


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
    "summaries, suggestions, and optimizations."
)

st.divider()


# ==================================================
# CODE INPUT
# ==================================================

st.subheader("📝 Enter Your Code")

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

    if code.strip():

        # ==================================================
        # STATIC ANALYSIS
        # ==================================================

        with st.spinner(
            "🔍 Analyzing your code..."
        ):

            result = analyze_code(code)
            quality = analyze_quality(code)

        if result is not None and quality is not None:

            st.success(
                "✅ Code analyzed successfully!"
            )


            # ==================================================
            # CODE METRICS
            # ==================================================

            st.divider()

            st.subheader(
                "📊 Code Metrics"
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


            # ==================================================
            # PERFORMANCE ANALYSIS
            # ==================================================

            st.divider()

            st.subheader(
                "⚡ Performance Analysis"
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Loop Depth",
                    result["loop_depth"]
                )

            with col2:
                st.metric(
                    "Time Complexity",
                    result["time_complexity"]
                )

            with col3:
                st.metric(
                    "Space Complexity",
                    result["space_complexity"]
                )


            # ==================================================
            # CODE QUALITY
            # ==================================================

            st.divider()

            st.subheader(
                "🏆 Code Quality"
            )

            col1, col2 = st.columns([1, 2])

            with col1:

                st.metric(
                    "Quality Score",
                    f"{quality['score']}/100"
                )

            with col2:

                st.progress(
                    quality["score"] / 100
                )


            # ==================================================
            # PERFORMANCE ISSUES
            # ==================================================

            st.divider()

            st.subheader(
                "⚠️ Performance Issues"
            )

            for issue in result["issues"]:

                st.warning(issue)


            # ==================================================
            # CODE QUALITY ISSUES
            # ==================================================

            st.divider()

            st.subheader(
                "🔎 Code Quality Issues"
            )

            for issue in quality["issues"]:

                st.warning(issue)


            # ==================================================
            # AI SUMMARY
            # ==================================================

            st.divider()

            st.subheader(
                "🤖 AI Code Summary"
            )

            try:

                with st.spinner(
                    "🤖 Gemini is analyzing your code..."
                ):

                    ai_summary = summarize_code(code)

                st.markdown(
                    ai_summary
                )

            except Exception as e:

                st.error(
                    "AI summary could not be generated."
                )

                st.caption(
                    f"Error: {str(e)}"
                )


            # ==================================================
            # AI SUGGESTIONS
            # ==================================================

            st.divider()

            st.subheader(
                "💡 AI Code Suggestions"
            )

            try:

                with st.spinner(
                    "🤖 Gemini is generating "
                    "improvement suggestions..."
                ):

                    ai_suggestions = suggest_improvements(
                        code
                    )

                st.markdown(
                    ai_suggestions
                )

            except Exception as e:

                st.error(
                    "AI suggestions could not be generated."
                )

                st.caption(
                    f"Error: {str(e)}"
                )


            # ==================================================
            # AI IMPROVED CODE
            # ==================================================

            st.divider()

            st.subheader(
                "✨ AI Improved Code"
            )

            try:

                with st.spinner(
                    "🤖 Gemini is generating "
                    "improved code..."
                ):

                    improved_code = generate_improved_code(
                        code
                    )

                st.code(
                    improved_code,
                    language="python"
                )

            except Exception as e:

                st.error(
                    "Improved code could not be generated."
                )

                st.caption(
                    f"Error: {str(e)}"
                )


            # ==================================================
            # STATIC SUGGESTIONS
            # ==================================================

            st.divider()

            st.subheader(
                "🛠️ Static Analyzer Suggestions"
            )

            for suggestion in quality["suggestions"]:

                st.info(
                    suggestion
                )


            # ==================================================
            # ADDITIONAL DETAILS
            # ==================================================

            st.divider()

            st.subheader(
                "📋 Additional Details"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.write(
                    f"**Variables:** "
                    f"{result['variables']}"
                )

            with col2:

                st.write(
                    f"**Total Loops:** "
                    f"{result['loops']}"
                )

            with col3:

                st.write(
                    f"**Total Conditions:** "
                    f"{result['conditions']}"
                )


        else:

            st.error(
                "❌ Invalid Python code. "
                "Please check your syntax."
            )


    else:

        st.warning(
            "⚠️ Please enter some code first."
        )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "Algolens — AI Driven Code Performance Analyzer"
)