🧠 CogniviseAI – Confusion-Aware Learning Assistant

Not just explaining concepts — diagnosing why learners are confused.

CogniviseAI is an AI-powered diagnostic learning assistant that identifies conceptual misunderstandings and provides targeted corrective explanations that help learners rebuild accurate mental models.

⸻

🎯 Problem

Many learners struggle not because information is unavailable, but because they develop incorrect mental models while learning new concepts.

When a misunderstanding forms early, it often persists and compounds over time. Most educational tools respond to confusion by:
	•	Repeating the same explanation
	•	Providing additional examples
	•	Offering generic hints

However, these approaches assume the learner simply needs more information.

In reality, the issue is often conceptual confusion — the learner has built an incorrect understanding of how a concept works.

Without identifying why the learner is confused, explanations become repetitive and ineffective. As a result, learners frequently resort to memorizing answers instead of understanding concepts, leading to fragile knowledge that breaks when applied to new problems.

⸻

💡 Solution

CogniviseAI focuses on diagnosing confusion rather than repeating explanations.

The system analyzes learner responses to identify the type of misunderstanding and then generates explanations designed to correct the learner’s mental model.

The platform:
	•	Generates diagnostic questions
	•	Analyzes learner responses
	•	Detects confusion patterns
	•	Classifies misunderstanding types
	•	Provides corrective explanations
	•	Tracks confusion trends over time

By addressing the root cause of misunderstanding, CogniviseAI helps learners build stronger conceptual understanding.

⸻

🏗 System Architecture

The system is designed using a cloud-based architecture on AWS.

User Browser
↓
AWS CloudFront
↓
AWS S3 – Static Frontend Hosting
↓
API Gateway
↓
AWS EC2 – FastAPI Backend API
↓
AI Engine

For the detailed architecture diagram see:

deployment/architecture.md

⸻

⚙️ Tech Stack

Frontend
	•	HTML
	•	CSS
	•	JavaScript

Backend
	•	Python
	•	FastAPI

AI Layer
	•	LLM-based reasoning engine

Cloud Infrastructure
	•	AWS S3 – static website hosting
	•	AWS CloudFront – content delivery network
	•	AWS API Gateway – API routing
	•	AWS EC2 – backend server
	•	Docker – containerization

⸻

📂 Repository Structure
ai_engine/        → AI reasoning and diagnostic logic
backend/          → FastAPI backend API
frontend/         → Web interface
deployment/       → AWS deployment configuration
docs/             → Project documentation


⸻

🎬 Demo Flow
	1.	User opens the web application.
	2.	The user selects a concept they want to understand.
	3.	The system generates a diagnostic question.
	4.	The user submits an answer.
	5.	The backend analyzes the response.
	6.	The AI engine detects the type of conceptual confusion.
	7.	The system provides a corrective explanation.
	8.	The dashboard tracks confusion trends and learning progress.

Detailed demo flow available in:

docs/demo-flow.md

⸻

🚀 Deployment

The project is designed to run on AWS cloud infrastructure.

Backend

Runs on AWS EC2 using Docker containers.

Frontend

Hosted on AWS S3 static website hosting and delivered via CloudFront.

Local Deployment

Run the application locally using Docker:

docker-compose up

⸻

📊 Future Enhancements
	•	Confusion analytics dashboard
	•	Personalized learning recommendations
	•	Expanded subject coverage
	•	Learning progress visualization
	•	Adaptive diagnostic questioning

⸻

👨‍💻 Contributors

Developed by a team working across:
	•	Frontend Development
	•	Backend Engineering
	•	AI Systems
	•	Cloud Infrastructure
