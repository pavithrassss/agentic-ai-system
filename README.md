# 🤖 Agentic AI System for Multi-Step Tasks

## 📌 Overview

This project is an Agentic AI System developed in Python that accepts a complex user request, breaks it into ordered tasks, assigns each task to a specialized AI agent, and generates the final output through a pipeline architecture.

The system demonstrates task decomposition, multiple specialized agents, streaming execution, graceful failure handling, and sequential pipeline execution using Google's Gemini API.

---

## ✨ Features

- Accepts complex multi-step user requests
- Automatically decomposes tasks
- Uses multiple AI agents
- Pipeline-based execution
- Streaming progress updates
- Retry mechanism for failure handling
- Modular and extensible architecture

---

## 🧠 Agents

### Planner Agent
Breaks the user's request into ordered execution steps.

### Retriever Agent
Researches and gathers information based on the execution plan.

### Analyzer Agent
Summarizes and analyzes the retrieved information.

### Writer Agent
Generates a professional LinkedIn post from the summary.

---

## ⚙️ Technologies Used

- Python
- Google Gemini API
- Rich (Terminal UI)
- Git
- GitHub

---

## 📂 Project Structure

```
agentic-ai-system/
│
├── agents/
│   ├── planner.py
│   ├── retriever.py
│   ├── analyzer.py
│   └── writer.py
│
├── config.py
├── pipeline.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/pavithrassss/agentic-ai-system.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GOOGLE_API_KEY=YOUR_API_KEY
```

Run

```bash
python main.py
```

---

## 📈 Workflow

User Input

↓

Planner Agent

↓

Retriever Agent

↓

Analyzer Agent

↓

Writer Agent

↓

Final Output

---

## ✅ Example Input

```
Research Artificial Intelligence in Healthcare.
Summarize it.
Create a LinkedIn Post.
```

---

## 📌 Future Improvements

- Async execution
- Web search integration
- PDF report generation
- More specialized agents

---

## 👩‍💻 Author

Pavithra

GitHub:
https://github.com/pavithrassss