# 🧠 CongniviseAI – System Design Document

## 1. Architecture Overview

CongniviseAI follows a modular layered architecture:


---

## 2. Component Design

### 2.1 FastAPI Layer
Handles:
- /diagnose
- /analyze
- /dashboard

Responsibilities:
- Input validation
- Dependency injection
- Database session management

---

### 2.2 LLM Engine (llm_engine.py)

Responsibilities:
- Generate diagnostic questions
- Use prompt engineering for gap detection
- Controlled model usage (gpt-4o-mini)

---

### 2.3 Confusion Classifier (classifier.py)

Inputs:
- Concept
- User answers

Process:
- Load taxonomy JSON
- Prompt AI to classify confusion
- Generate corrective explanation

Output:
- Confusion Type
- Explanation
- Correct Model
- Practice Question

---

### 2.4 Database Layer

Schema:

UserSession:
- id (int)
- concept (string)
- confusion_type (string)
- created_at (datetime)

Purpose:
- Track user misconceptions
- Enable analytics

---

## 3. Data Flow

1. User enters concept
2. Backend calls LLM to generate diagnostic questions
3. User submits answers
4. Classifier identifies confusion type
5. Result stored in database
6. Dashboard aggregates data

---

## 4. Scalability Plan

Future Enhancements:

- Replace SQLite with PostgreSQL
- Add user authentication
- Add adaptive learning paths
- Add performance metrics tracking
- Add real-time dashboard visualization

---

## 5. Security Considerations

- Environment variable storage for API keys
- No sensitive data persistence
- CORS enabled for frontend integration
- Controlled LLM prompt formatting

---

## 6. Design Decisions

| Decision | Reason |
|----------|--------|
| FastAPI | High performance, async support |
| SQLAlchemy | ORM flexibility |
| JSON Taxonomy | Easy extensibility |
| AI-based classification | Dynamic conceptual detection |

---

## 7. Unique Innovation

ClarityAI does not merely explain concepts.

It identifies:
- The specific cognitive gap
- The learner’s incorrect mental model
- The targeted corrective strategy

This moves from content delivery to cognitive diagnosis.
