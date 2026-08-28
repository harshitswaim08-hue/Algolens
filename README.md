# 🔍 Algolens

## AI Driven Code Performance Analyzer

Algolens is an AI-powered code performance analyzer that analyzes Python code and provides code metrics, complexity analysis, quality evaluation, AI-powered suggestions, optimized code, and automated reports.

---

## 🚀 Features

- 📊 Code Metrics Analysis
- ⚡ Time Complexity Analysis
- 💾 Space Complexity Analysis
- 🏆 Static Code Quality Evaluation
- 🤖 AI-Based Code Summary
- 💡 AI Improvement Suggestions
- ✨ AI-Generated Improved Code
- 🌲 ML-Based Code Quality Prediction
- 📄 Text Analysis Report
- 📑 PDF Analysis Report

---

## 🧠 Machine Learning

Algolens uses a **Random Forest Regression model** to predict code quality.

### Dataset

- Total samples: 1000
- Features include:
  - Lines of code
  - Functions
  - Loops
  - Conditions
  - Variables
  - Loop depth
  - Time complexity
  - Space complexity

### Model Performance

- **Mean Absolute Error (MAE): 2.22**
- **R² Score: 0.96**

The trained model is stored as:

```text
ml/model.pkl


🛠️ Technologies Used
Python
Streamlit
Google Gemini AI
Scikit-learn
Random Forest
Pandas
Joblib
ReportLab
Plotly
Radon

📁 Project Structure
Algolens/
│
├── analyzer/
│   ├── code_parser.py
│   └── quality.py
│
├── ai/
│   └── ai_analyzer.py
│
├── ml/
│   ├── dataset.csv
│   ├── generate_dataset.py
│   ├── inspect_dataset.py
│   ├── train_model.py
│   ├── test_model.py
│   ├── test_predictor.py
│   ├── ml_predictor.py
│   └── model.pkl
│
├── reports/
│   ├── report_generator.py
│   └── pdf_report.py
│
├── sample_codes/
├── utils/
│
├── app.py
├── app_backup.py
├── test_ai.py
├── requirements.txt
├── README.md
└── .gitignore




⚙️ Installation

Clone the repository:

git clone https://github.com/harshitswaim08-hue/Algolens.git

Go to the project directory:

cd Algolens

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt
🔐 API Key Setup

Create a .env file in the project root and add your Gemini API key.

GEMINI_API_KEY

▶️ Run the Application

Start the Streamlit application:
streamlit run app.py

The application will open in your browser.

📊 Application Workflow
Python Code
     ↓
AST-Based Code Analysis
     ↓
Code Metrics & Complexity
     ↓
Static Quality Analysis
     ↓
ML Quality Prediction
     ↓
Gemini AI Analysis
     ↓
Suggestions & Improved Code
     ↓
Text/PDF Report


🤖 AI Analysis

Algolens uses Google Gemini AI to provide:

Code summary
Improvement suggestions
Optimized/improved code

This complements the static analyzer and machine-learning-based quality prediction.

📈 Analysis Dashboard

The application provides:

Overall Score
Code Quality Score
ML Quality Prediction
Lines of Code
Number of Functions
Number of Loops
Number of Conditions
Time Complexity
Space Complexity
Loop Depth
Performance Issues
Code Quality Issues


📄 Automated Reports

Algolens can generate:

Text Report

A downloadable text-based analysis report containing code metrics, quality analysis, performance analysis, and AI insights.

PDF Report

A professional PDF report containing the complete analysis results, AI suggestions, and improved code.

🎯 Project Objective

The objective of Algolens is to provide developers and students with an automated platform for understanding code performance, identifying potential issues, evaluating code quality, and receiving AI-powered optimization suggestions.

🌟 Key Benefits
Easy-to-use web interface
Automated code analysis
Complexity detection
Machine-learning-based quality prediction
AI-powered recommendations
Automated report generation
Helps users understand and improve their code


🔮 Future Scope

Support for additional programming languages
Advanced complexity analysis
More machine-learning models
Code quality visualization
GitHub repository integration
Automated code review
Performance benchmarking
Cloud deployment


👨‍💻 Project
Algolens — AI Driven Code Performance Analyzer
Developed as an academic group project.