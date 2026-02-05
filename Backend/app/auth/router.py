from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.auth.service import verify_google_token, get_or_create_user_from_google
from app.core.security import create_access_token, verify_token
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/auth", tags=["Authentication"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class GoogleLoginRequest(BaseModel):
    token: str

@router.post("/google")
def google_login(request: GoogleLoginRequest, db: Session = Depends(get_db)):
    # 1. Verify Google token
    id_info = verify_google_token(request.token)
    if not id_info:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Google token"
        )
    
    # 2. Get or create user in our DB
    user = get_or_create_user_from_google(db, id_info)
    
    # 3. Create our own JWT
    access_token = create_access_token(data={"sub": user.email, "user_id": user.user_id, "role": user.role})
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }

@router.get("/me")
def get_me(token: str, db: Session = Depends(get_db)):
    # This is a simple implementation, usually you'd use a dependency for this
    payload = verify_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    email = payload.get("sub")
    from app.models.user import User
    user = db.query(User).filter(User.email == email).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user
