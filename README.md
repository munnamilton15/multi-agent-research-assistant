# Multi-Agent Research Assistant

An AI-powered multi-agent research system built with CrewAI, Google Gemini, and web search.

The system uses multiple specialized AI agents that collaborate sequentially to research a topic, analyze evidence, fact-check claims, and generate a structured technical report.

---

## 🚀 Project Overview

The Multi-Agent Research Assistant automates the research workflow using four specialized AI agents.

Instead of asking a single AI model to perform the entire task, the system divides the workflow into specialized responsibilities.

### Agent Pipeline

Research → Analysis → Fact Check → Report

```text
                    Research Topic
                         │
                         ▼
              ┌─────────────────────┐
              │  Research Librarian │
              │     Web Search      │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Research Analyst  │
              │ Evidence Analysis   │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │    Fact Checker     │
              │ Verify Claims       │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Technical Writer    │
              │ Final Report        │
              └──────────┬──────────┘
                         │
                         ▼
                  Markdown Report
