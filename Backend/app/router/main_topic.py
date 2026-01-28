from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.main_topic import MainTopicCreate, MainTopicOut
from app.services.main_topic import create_main_topic, get_main_topics, get_main_topic, update_main_topic, delete_main_topic

router = APIRouter(prefix="/main-topics", tags=["Main Topics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MainTopicOut)
def add_main_topic(data: MainTopicCreate, db: Session = Depends(get_db)):
    return create_main_topic(db, data)

@router.get("/", response_model=list[MainTopicOut])
def read_main_topics(db: Session = Depends(get_db)):
    return get_main_topics(db)

@router.get("/{main_topic_id}", response_model=MainTopicOut)
def read_main_topic(main_topic_id: str, db: Session = Depends(get_db)):
    return get_main_topic(db, main_topic_id)

@router.put("/{main_topic_id}", response_model=MainTopicOut)
def edit_main_topic(main_topic_id: str, data: MainTopicCreate, db: Session = Depends(get_db)):
    return update_main_topic(db, main_topic_id, data)

@router.delete("/{main_topic_id}")
def remove_main_topic(main_topic_id: str, db: Session = Depends(get_db)):
    delete_main_topic(db, main_topic_id)
    return {"status": "deleted"}
