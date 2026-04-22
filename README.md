# AutoStream AI Agent

## Features
- Intent detection
- RAG-based answers
- Lead capture tool

## How to Run
1. Create virtual environment
2. Install requirements:
   pip install -r requirements.txt
3. Run:
   python app.py

## Architecture
This project uses rule-based intent detection and local JSON-based RAG.
State is managed using a Python dictionary.

## WhatsApp Integration
Use Twilio API with webhook to connect chatbot.
