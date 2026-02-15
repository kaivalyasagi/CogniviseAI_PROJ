# 📌 ClarityAI – Requirements Document

## 1. Problem Statement

Students learning Data Structures & Algorithms often struggle not because of lack of information, but because of hidden conceptual misunderstandings.

ClarityAI identifies *why* a learner is confused and provides targeted corrective explanations.

---

## 2. Objectives

- Detect conceptual misunderstanding using AI
- Classify confusion into predefined taxonomy categories
- Provide targeted explanations
- Track user learning patterns
- Visualize confusion trends

---

## 3. Functional Requirements

### 3.1 User Input
- User enters a concept (e.g., Recursion)
- System generates diagnostic questions

### 3.2 Diagnostic Engine
- AI generates 3 concept-specific diagnostic questions
- Questions aim to expose mental model gaps

### 3.3 Confusion Classification
- User submits answers
- AI classifies confusion into predefined types
- Returns:
  - Confusion Type
  - Explanation
  - Correct Mental Model
  - Practice Question

### 3.4 Data Persistence
- Store:
  - Concept
  - Confusion Type
  - Timestamp

### 3.5 Analytics Dashboard
- Aggregate confusion data
- Show most frequent confusion types

---

## 4. Non-Functional Requirements

- API response time < 3 seconds
- Modular architecture
- Clean REST API structure
- Scalable database design
- Secure API key handling via environment variables

---

## 5. Tech Stack

| Layer | Technology |
|--------|------------|
| Backend | FastAPI |
| AI Engine | OpenAI API |
| Database | SQLite |
| ORM | SQLAlchemy |
| Frontend | Next.js |
| Environment | Python venv |

---

## 6. Constraints

- Must run locally
- No hardcoded API keys
- No large infrastructure required
