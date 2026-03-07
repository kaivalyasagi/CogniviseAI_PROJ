# Cognivise AI – AWS Architecture

## System Architecture

The system is deployed using AWS cloud infrastructure.

Frontend is hosted as a static website.
Backend API runs on an EC2 instance using FastAPI.
AI processing is handled within the backend service.

## Architecture Flow

User Browser
      ↓
Frontend (AWS S3 Static Hosting)
      ↓
API Requests
      ↓
AWS API Gateway
      ↓
EC2 Instance
      ↓
FastAPI Backend
      ↓
AI Engine
