# VulnStore AI

A deliberately vulnerable RAG (Retrieval Augmented Generation) application built for AI Security research and learning.

## Technology Stack

- FastAPI
- ChromaDB
- Sentence Transformers
- Ollama
- Llama3

## Security Focus Areas

- OWASP LLM Top 10
- MITRE ATLAS
- Prompt Injection
- Sensitive Data Disclosure
- Data Poisoning
- Knowledge Extraction
- AI SSDLC

## Architecture

User → FastAPI → Retriever → ChromaDB → Llama3 → Response

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 ingest.py
uvicorn app:app --reload