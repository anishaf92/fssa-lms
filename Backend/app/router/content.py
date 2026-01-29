from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.content import ContentCreate, ContentOut
from app.services.content import create_content, get_contents, get_content, update_content, delete_content

router = APIRouter(prefix="/contents", tags=["Contents"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ContentOut)
def add_content(data: ContentCreate, db: Session = Depends(get_db)):
    return create_content(db, data)

@router.get("/", response_model=list[ContentOut])
def read_contents(db: Session = Depends(get_db)):
    return get_contents(db)

@router.get("/{content_id}", response_model=ContentOut)
def read_content(content_id: str, db: Session = Depends(get_db)):
    return get_content(db, content_id)

@router.put("/{content_id}", response_model=ContentOut)
def edit_content(content_id: str, data: ContentCreate, db: Session = Depends(get_db)):
    return update_content(db, content_id, data)

@router.delete("/{content_id}")
def remove_content(content_id: str, db: Session = Depends(get_db)):
    delete_content(db, content_id)
    return {"status": "deleted"}
