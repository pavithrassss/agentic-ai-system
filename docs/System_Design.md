# System Design Document

## Project Title
Agentic AI System for Multi-Step Tasks

---

# Objective

The objective of this project is to build an Agentic AI system capable of accepting a complex user request, breaking it into smaller tasks, assigning each task to a specialized AI agent, and generating the final output using a pipeline-based architecture.

---

# Architecture

```
                +------------------+
                |    User Input    |
                +------------------+
                         |
                         v
                +------------------+
                | Planner Agent    |
                +------------------+
                         |
                         v
                +------------------+
                | Retriever Agent  |
                +------------------+
                         |
                         v
                +------------------+
                | Analyzer Agent   |
                +------------------+
                         |
                         v
                +------------------+
                | Writer Agent     |
                +------------------+
                         |
                         v
                +------------------+
                | Final Output     |
                +------------------+
```

---

# Components

## Planner Agent
- Accepts the user's request.
- Breaks the request into ordered execution steps.

---

## Retriever Agent
- Uses the generated execution plan.
- Collects relevant information using the Gemini API.

---

## Analyzer Agent
- Processes the retrieved information.
- Produces a concise summary.

---

## Writer Agent
- Converts the summary into a professional LinkedIn post.

---

# Pipeline Flow

1. User enters a complex task.
2. Planner creates an execution plan.
3. Retriever gathers information.
4. Analyzer summarizes the research.
5. Writer generates the final content.
6. Results are displayed to the user.

---

# Failure Handling

The system includes retry logic.

If an AI agent fails:
- The request is retried up to three times.
- If all retries fail, an error is displayed gracefully without crashing the application.

---

# Streaming Output

The pipeline streams progress by displaying the completion status of each agent, allowing the user to monitor execution step by step.

---

# Technologies Used

- Python
- Google Gemini API
- Rich
- Git
- GitHub

---

# Future Improvements

- Async execution
- Additional specialized agents
- Web search integration
- PDF report generation
- Database support