# EduFlow — Smart Student Productivity Agent
# Kaggle: Agents Intensive – Capstone Project (2025)

EduFlow is a lightweight multi-agent system designed to improve the academic productivity of students.  
It automates PDF summarization, assignment tracking, daily planning, simple study-material search, and observability — all inside a single clean notebook that judges can run instantly.

This project is submitted under the Concierge Agents Track.

---

# 🚀 Project Overview

Students often struggle with:
- Long and unstructured study materials  
- Managing assignments and deadlines  
- Planning their daily study/work schedule  
- Finding quality resources online  
- Keeping everything organized in one place  

EduFlow solves these problems using a set of specialized agents working together.

# ✔ Notes Agent  
Extracts and summarizes PDF notes into short, clean summaries.

# ✔ Tracker Agent  
Stores assignments, deadlines, and task metadata using a simple memory structure.

# ✔ Gemini LLM Integration
EduFlow now uses Gemini 1.5 Flash for PDF summarization.  
The notebook loads the API key securely from Kaggle Secrets and calls the Gemini model for high-quality summaries.

# ✔ Planner Agent  
Generates a daily plan using:
- Class timetable  
- Pending assignments  
- Basic rule-based logic  

# ✔ Search Agent  
Searches the web (DuckDuckGo HTML) for relevant study resources.

# ✔ Observability Agent  
Logs every action using structured JSON logs so judges can see reasoning & behavior.

---

Notebook Demo: https://www.kaggle.com/code/donalthenammackal/eduflow-scarfall  
