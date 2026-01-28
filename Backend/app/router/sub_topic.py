from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.sub_topic import SubTopicCreate, SubTopicOut
from app.services.sub_topic import create_sub_topic, get_sub_topics, get_sub_topic, update_sub_topic, delete_sub_topic

router = APIRouter(prefix="/sub-topics", tags=["Sub Topics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SubTopicOut)
def add_sub_topic(data: SubTopicCreate, db: Session = Depends(get_db)):
    return create_sub_topic(db, data)

@router.get("/", response_model=list[SubTopicOut])
def read_sub_topics(db: Session = Depends(get_db)):
    return get_sub_topics(db)

@router.get("/{sub_topic_id}", response_model=SubTopicOut)
def read_sub_topic(sub_topic_id: str, db: Session = Depends(get_db)):
    return get_sub_topic(db, sub_topic_id)

@router.put("/{sub_topic_id}", response_model=SubTopicOut)
def edit_sub_topic(sub_topic_id: str, data: SubTopicCreate, db: Session = Depends(get_db)):
    return update_sub_topic(db, sub_topic_id, data)

@router.delete("/{sub_topic_id}")
def remove_sub_topic(sub_topic_id: str, db: Session = Depends(get_db)):
    delete_sub_topic(db, sub_topic_id)
    return {"status": "deleted"}
