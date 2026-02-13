# Weather Agent API

A FastAPI-based weather backend demonstrating a developer-controlled agent architecture.

## Overview

This project began as an experiment with LLM tool-calling (model-controlled agent design).  
During development, instability in model-driven execution highlighted the importance of architectural control.

The final design uses a **developer-controlled agent pattern**, where:

- The LLM (when used) extracts structured data only.
- Execution logic remains fully deterministic in Python.
- Tools are invoked explicitly by the developer.
- The model never has direct execution authority.

This separation improves stability, predictability, and safety.

---

## Architecture

User Input  
↓  
(LLM – optional parsing layer)  
↓  
Developer-controlled execution layer  
↓  
Weather tool abstraction  
↓  
Structured API response  

The model influences data, not system behavior.

---

## Features

- REST API built with FastAPI
- Structured weather lookup tool
- Input normalization
- Swagger auto-documentation
- Clear separation between parsing and execution
- Clean Git hygiene (.gitignore, no cache files)

---

## Run Locally

```bash
pip install -r requirements.txt
python -m uvicorn app:app --reload
