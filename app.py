import streamlit as st
import os
import sqlite3
import re
import google.generativeai as genai

# Set API key from environment
genai.configure(api_key=os.getenv('API_KEY'))

# Prompt setup (Gemini should return only SQL query)
prompt = ["""
You are an expert in converting English questions to SQL queries.
The SQL database has the name STUDENTS with the following columns - NAME, CLASS, Marks, Company.
Respond with only the SQL query. Do NOT provide explanation or extra text.

Examples:
Q: How many records are present?
A: SELECT COUNT(*) FROM STUDENTS;

Q: Show names of students with marks above 80.
A: SELECT NAME FROM STUDENTS WHERE Marks > 80;
"""]

# Get Gemini response
def get_response(que, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    response = model.generate_content([prompt[0], que])
    return response.text

# Run SQL query
def read_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

# Home Page
def page_home():
    st.markdown("""
    <style>
        .main-title { text-align: center; color: #4CAF50; font-size: 2.5em; }
        .sub-title { text-align: center; color: #4CAF50; font-size: 1.5em; }
        .offerings { padding: 20px; color: white; }
        .offerings h2 { color: #4CAF50; }
        .offerings ul { list-style-type: none; padding: 0; }
        .offerings li { margin: 10px 0; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='main-title'>Welcome to IntelliSQL</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-title'>Revolutionizing Database Querying with Advanced LLM Capabilities</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col2:
        st.markdown("""
        <div class='offerings' style="background-color:#0E1117; padding: 20px; border-radius: 10px;">
            <h2 style="color:white;">Wide Range of Offerings</h2>
            <ul style="color:white; font-size:16px;">
                <li>📌 Intelligent Query Assistance</li>
                <li>📥 Data Exploration and Insights</li>
                <li>⚡ Efficient Data Retrieval</li>
                <li>🚀 Performance Optimization</li>
                <li>📖 Syntax Suggestions</li>
                <li>📊 Trend Analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# About Page
def page_about():
    st.markdown("""
    <style>.content { color: white; }</style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='color: #4CAF50;'>About IntelliSQL</h1>", unsafe_allow_html=True)
    st.markdown("<div class='content'>", unsafe_allow_html=True)
    st.markdown("""
    <h2>IntelliSQL is an innovative project aimed at revolutionizing database querying using advanced Language Model capabilities.</h2>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.image("https://download.logo.wine/logo/Oracle_SQL_Developer/Oracle_SQL_Developer-Logo.wine.png", use_container_width=True)

# Query Assistant Page
def page_intelligent_query_assistance():
    st.markdown("<h1 style='color: #4CAF50;'>Intelligent Query Assistance</h1>", unsafe_allow_html=True)
    st.write("IntelliSQL enhances the querying process by providing intelligent assistance to users. Whether novice or expert, this tool simplifies SQL access.")

    col1, col2 = st.columns([2, 1])

    with col1:
        que = st.text_input("Enter Your Query:")
        submit = st.button("Get Answer", help="Click to retrieve the SQL data")

        if submit or que:
            try:
                # Get Gemini output
                raw_response = get_response(que, prompt)

                # Extract SQL query (first line starting with SELECT, INSERT etc.)
                match = re.search(r"(SELECT|INSERT|UPDATE|DELETE).*?;", raw_response, re.IGNORECASE | re.DOTALL)
                if match:
                    sql_query = match.group(0).strip()
                    st.write("**Generated SQL Query:**")
                    st.code(sql_query, language='sql')

                    # Run query
                    result = read_query(sql_query, "data.db")
                    st.subheader("The Response is:")
                    st.table(result)
                else:
                    st.subheader("Error:")
                    st.error("Could not extract a valid SQL query from the response.")
            except Exception as e:
                st.subheader("Error:")
                st.error(f"An error occurred: {e}")

    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/9850/9850877.png", use_container_width=True)

# Main Controller
def main():
    st.set_page_config(page_title="IntelliSQL", page_icon="💡", layout="wide")
    st.sidebar.title("Navigation")

    pages = {
        "Home": page_home,
        "About": page_about,
        "Intelligent Query Assistance": page_intelligent_query_assistance,
    }

    selection = st.sidebar.radio("Go to", list(pages.keys()))
    pages[selection]()

if __name__ == "__main__":
    main()
