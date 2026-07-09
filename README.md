# About

This project is a simple impementation of ai-agent pipeline. The final goal is to use this simple pipeline to work with documents via complex interaction with UI.

# Interaction

User sends a request to server. Server handles request and launches agent pipeline. After completing pipeline server sends response.

# How pipeline work

It is a python module, which interacts with llm server and is responsible for entire ai workflow. It launches agent sessions and provides ability to interact with toolchains.

# How to run

```bash
uvicorn src.server:app --reload
```

```bash
python -m uvicorn src.server:app --reload
```

```bash
python src/server.py
```