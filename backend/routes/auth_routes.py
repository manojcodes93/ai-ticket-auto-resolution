from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schemas import LoginSchema
from backend.auth import authenticate_user

router = APIRouter()


@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):

    user = authenticate_user(data.email, data.password, db)

    if not user:
        return {"error": "Invalid credentials"}

    return {
        "id": user.id,
        "name": user.name,
        "role": user.role
    }