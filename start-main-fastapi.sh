#!/bin/sh

uvicorn main-fastapi:app --reload --host 0.0.0.0 --port 8000
# localhost:8000