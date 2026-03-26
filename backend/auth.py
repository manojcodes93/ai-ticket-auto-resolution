from sqlalchemy.orm import Session
from backend.models import User


def authenticate_user(email: str, password: str, db: Session):

    user = db.query(User).filter(User.email == email).first()

    if not user or user.password != password:
        return None

    return user