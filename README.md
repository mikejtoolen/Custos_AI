# Custos AI - Enterprise AI System

An intelligent agentic system designed to analyze customer churn risk, assess financial exposure, and make automated business decisions using LangChain.

## 🚀 Overview

This project leverages the power of Large Language Models (LLMs) and agentic workflows to help telecom businesses:
- **Summarize customer data**: Retrieve detailed profiles including churn flags, tenure, usage intensity, and support history.
- **Analyze Customer Risk**: Retrieve detailed profiles including churn flags, tenure, usage intensity, and support history.
- **Assess Financial Impact**: Calculate total and average monthly revenue exposure.
- **Make Data-Driven Decisions**: An autonomous agent analyzes data to recommend actions (e.g., retention offers) and stores these decisions in an enterprise memory for future reference.


## 🛠️ Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Teleco_churn
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Configuration:**
    Create a `.env` file in the root directory and add your Groq API key:
    ```env
    GROQ_API_KEY=your_api_key_here
    ```

5.  **Initialize the Database:**
    Run the ingestion script to populate the SQLite database from raw data:
    ```bash
    python ingestion/ingest_2_sqlite.py
    ```

## ▶️ Usage

1.  **Start the Application:**
    ```bash
    streamlit run run.py
    ```

2.  **Interact with the System:**
    - Enter natural language queries in the web interface.
    - **Examples:**
        - *"Analyze the risk profile for customer 7795-CFOCW"* (Analysis Mode)
        - *"What is our total financial exposure?"* (Analysis Mode)
        - *"Make a decision for churn risk customer 7795-CFOCW"* (Decision Mode - triggers Agent)

## 📊 Database Schema

The SQLite database `data/processed/enterprise_intelligence.db` contains linked tables for `customers`, `billing_financials`, `services_usage`, and `support_experience`, allowing for complex SQL queries by the AI agent.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.