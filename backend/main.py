from fastapi import FastAPI
import sys
import os
from sqlalchemy import text

# ✅ Add root path (to access model folder)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Import AI + DB
from model.ai_engine import solve_ticket
from database import SessionLocal

app = FastAPI()

# ---------------------------
# Basic test route
# ---------------------------
@app.get("/")
def home():
    return {"message": "Backend is running"}

# ---------------------------
# DB connection test
# ---------------------------
@app.get("/test_db")
def test_db():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        return {"message": "Database connected successfully"}
    except Exception as e:
        return {"error": str(e)}

# ---------------------------
# AI prediction API
# ---------------------------
@app.post("/predict_ticket")
def predict_ticket(ticket: str):
    result = solve_ticket(ticket)
    return result