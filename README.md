# 🚀 ATS + RAG Resume Chatbot

An **AI-powered ATS (Applicant Tracking System) + RAG Chatbot** that evaluates resumes against job descriptions and provides intelligent, context-aware feedback.

---

## 🧠 Project Overview

This project combines **NLP, Machine Learning, and Retrieval-Augmented Generation (RAG)** to simulate a real-world ATS system.

It allows users to:

* Upload a resume (PDF)
* Enter a job description
* Get an ATS score
* Identify missing skills
* Chat with the system for personalized feedback

---

## 🔥 Key Features

✅ Resume Parsing (PDF → Text)
✅ Dynamic Skill Extraction (Multi-domain)
✅ ATS Score Calculation
✅ Missing Skill Detection
✅ Semantic Matching using Sentence-BERT
✅ RAG-based Chatbot (Context-aware answers)
✅ Multi-domain Support (Tech, Marketing, Finance, etc.)

---

## 🏗️ Architecture

```
Resume + Job Description
        ↓
Text Cleaning (NLP)
        ↓
Skill Extraction
        ↓
Semantic Similarity (BERT)
        ↓
ATS Score Calculation
        ↓
RAG Pipeline (LangChain + Chroma)
        ↓
LLM (Groq - LLaMA)
        ↓
Chatbot Response
```

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend Logic**: Python
* **NLP**: Regex, Text Processing
* **ML**: Sentence-Transformers (BERT)
* **Vector DB**: ChromaDB
* **RAG Framework**: LangChain
* **LLM**: Groq (LLaMA 3)

---

## 📂 Project Structure

```
ats-rag-chatbot/
│
├── app.py              # Main Streamlit app
├── nlp.py              # Text cleaning & skill extraction
├── ml.py               # Similarity & ATS scoring
├── rag.py              # RAG pipeline (vector DB)
├── chatbot.py          # LLM interaction
├── skills.json         # Multi-domain skill dataset
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/ats-rag-chatbot.git
cd ats-rag-chatbot

pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 📊 Example Output

* **ATS Score**: 72%
* **Missing Skills**: Deep Learning, NLP
* **Chatbot**: Provides improvement suggestions

---

## 💡 How It Works

* Extracts skills from resume & job description
* Uses semantic similarity for matching
* Identifies missing skills
* Retrieves relevant context using RAG
* Generates intelligent responses via LLM

---

## 🏆 Why This Project Stands Out

* Real-world ATS simulation
* Domain-independent (works for all job roles)
* Combines NLP + ML + GenAI
* Production-ready architecture

---

## 🚀 Future Improvements

* Resume ranking system
* Multi-resume comparison
* Job role detection
* Skill recommendation engine
* Deployment (AWS / Render)

---

## 👨‍💻 Author

**Tanuj Kumar**
AI/ML Enthusiast | NLP | GenAI

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
