# AI-Generated Code Vulnerability Detector

This web application demonstrates the research idea of detecting security vulnerabilities in AI-generated code, as outlined in the provided literature review. It uses Bandit, a Python security linter, as a baseline tool for vulnerability detection.

## Features

- Web-based interface to input Python code
- Static analysis using Bandit to detect common security issues
- Local execution (no internet required for analysis)

## Installation

1. Ensure you have Python 3.7+ installed.
2. Activate the virtual environment: `source .venv/bin/activate`
3. Install dependencies: `pip install flask bandit`

## Running the App

1. Activate the virtual environment: `source .venv/bin/activate`
2. Run the app: `python app.py`
3. Open your browser and go to `http://127.0.0.1:5000/`

## Usage

1. Paste Python code into the text area.
2. Click "Analyze Code" to run Bandit analysis.
3. View the results below, which will show any detected vulnerabilities.

## Research Context

This app serves as a prototype for the research project on transformer-based vulnerability detection in AI-generated Python code. The literature review highlights the need for automated tools to identify security flaws in code produced by LLMs like GitHub Copilot. While this implementation uses a rule-based tool (Bandit), the research aims to develop transformer models (CodeBERT, GraphCodeBERT, VulBERTa) for more advanced detection.

## Future Enhancements

- Integrate pre-trained transformer models for vulnerability detection
- Add support for multiple programming languages
- Implement explainability features
- Create a dataset of AI-generated vulnerable code for training