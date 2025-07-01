IntelliSQL: Intelligent SQL Querying with LLMs Using Gemini Pro

🔍 Overview

IntelliSQL is a smart, AI-powered SQL query assistant that helps users interact with databases using natural language. It uses Google's Gemini Pro LLM to convert plain English questions into SQL queries and executes them on an SQLite3 database.
________________________________________
🚀 Features

•	📌 Intelligent Query Assistance

•	📥 Data Exploration and Insights

•	⚡ Efficient Data Retrieval

•	🚀 Performance Optimization

•	📖 Syntax Suggestions

•	📊 Trend Analysis
________________________________________
📘 Project Flow
1.	User inputs a natural language query.
2.	Gemini Pro generates a valid SQL statement.
3.	SQL query is executed on an SQLite3 database.
4.	Results are displayed back to the user.
________________________________________
📦 Requirements Specification

•	Python 3.8+

•	Streamlit

•	sqlite3

•	google-generativeai

•	dotenv (for .env file handling)

Install all dependencies using:

pip install -r requirements.txt
________________________________________


🔑 Initialization of Google API Key

Create a .env file:

API_KEY=your_google_gemini_api_key

This key is loaded using:

import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))
________________________________________
🗃️ Database Creation Using SQLite3

The database is created using sql.py. It sets up a STUDENTS table with sample data:

CREATE TABLE STUDENTS(Name TEXT, Class TEXT, Marks INTEGER, Company TEXT);

Run this script before starting the app:

python sql.py
________________________________________
🤖 Interfacing With Pre-Trained Model

Gemini Pro (via Google Generative AI API) is used to generate SQL queries from English text.

response = model.generate_content([prompt[0], que])
________________________________________
⚠️ Problems We Faced

•	❌ Gemini returning extra explanation text

•	❌ Invalid SQL due to multi-line responses

•	❌ Missing table errors in SQLite

✅ How We Solved Them

•	✅ Used regex to extract only valid SQL from Gemini responses

•	✅ Rewrote prompts to force Gemini to respond with SQL only

•	✅ Handled SQL exceptions and added validation
________________________________________

🧑 Team Members

•	Harshvir Singh

•	Nishil Gangrade

•	Soumya Ajmera
________________________________________
📂 Project Structure

IntelliSQL/

├── app.py

├── sql.py

├── data.db

├── .env

├── requirements.txt

├── screenshots/
________________________________________
✅ Conclusion

IntelliSQL bridges the gap between natural language and complex database queries using LLMs. It is an innovative solution for non-tech users to interact with SQL databases effortlessly.
________________________________________
🔗 GitHub Repository

https://github.com/18warrior/IntelliSQL

