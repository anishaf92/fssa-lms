from sqlalchemy.orm import Session
from google.oauth2 import id_token
from google.auth.transport import requests
from app.core.config import GOOGLE_CLIENT_ID
from app.models.user import User
from app.core.security import create_access_token
import uuid

def verify_google_token(token: str):
    try:
        # Specify the GOOGLE_CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        # userid = idinfo['sub']
        return idinfo
    except ValueError:
        # Invalid token
        return None

def get_or_create_user_from_google(db: Session, id_info: dict):
    email = id_info.get("email")
    name = id_info.get("name")
    
    user = db.query(User).filter(User.email == email).first()
    
    if not user:
        # Create user if it doesn't exist
        user = User(
            user_id=str(uuid.uuid4()),
            email=email,
            name=name,
            role="student" # Default role
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    
    return user
