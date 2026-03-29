from sqlalchemy.orm import Session
from backend.models import User
from datetime import datetime, timedelta
import jwt

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"


def authenticate_user(username: str, password: str, db: Session):
    user = db.query(User).filter(User.email == username).first()

    if not user:
        return None

    if user.password != password:
        return None

    return user


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=2)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt