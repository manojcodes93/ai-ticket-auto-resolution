from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from backend.database import SessionLocal
from backend.models import User

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")

        db = SessionLocal()
        user = db.query(User).filter(User.email == email).first()
        db.close()

        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return user

    except:
        raise HTTPException(status_code=401, detail="Invalid token")