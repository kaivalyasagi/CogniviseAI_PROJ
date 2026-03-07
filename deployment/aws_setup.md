# AWS Deployment Guide

## Architecture

Frontend → AWS S3  
Backend → AWS EC2  
AI Engine → Backend service  

## Deployment Steps

1. Launch EC2 instance
2. Install Docker
3. Clone GitHub repo

git clone <repo-url>

4. Run application

cd deployment
docker-compose up

Backend will run on port 8000.
