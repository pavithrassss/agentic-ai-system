# Post-Mortem Document

## Project Title
Agentic AI System for Multi-Step Tasks

---

## Overview

This project was developed to demonstrate an Agentic AI system capable of solving complex, multi-step tasks by coordinating multiple specialized AI agents through a pipeline architecture.

---

## Scaling Issue

As the number of specialized agents or concurrent user requests increases, the sequential pipeline can become slower because each agent waits for the previous one to finish.

In the future, asynchronous execution and task queues could be introduced to improve scalability and reduce response time.

---

## Design Change in Hindsight

If redesigning the project, I would separate the AI model interaction into a dedicated service layer instead of calling the model directly inside each agent.

This would improve code reusability, testing, and make it easier to support multiple AI providers.

---

## Trade-off 1

### Simplicity vs Performance

I chose a sequential pipeline because it is easier to understand, debug, and maintain.

Although asynchronous execution could improve performance, the sequential approach makes the execution flow much clearer.

---

## Trade-off 2

### Modularity vs API Calls

Each responsibility was assigned to a separate agent (Planner, Retriever, Analyzer, Writer).

This improves modularity and makes the architecture extensible, but it also increases the number of API calls and overall execution time.

---

## Lessons Learned

- Designing modular AI systems improves maintainability.
- Retry mechanisms make AI applications more reliable.
- Clear separation of responsibilities simplifies debugging.
- Pipeline architecture makes multi-step AI workflows easier to understand and extend.

---

## Future Improvements

- Async execution
- Parallel agent execution where possible
- Manual batching optimization
- Logging and monitoring
- Support for multiple LLM providers