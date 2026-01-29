from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.course import CourseCreate, CourseOut
from app.services.course import create_course, get_courses, get_course, update_course, delete_course

router = APIRouter(prefix="/courses", tags=["Courses"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CourseOut)
def add_course(data: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db, data)

@router.get("/", response_model=list[CourseOut])
def read_courses(db: Session = Depends(get_db)):
    return get_courses(db)

@router.get("/{course_id}", response_model=CourseOut)
def read_course(course_id: str, db: Session = Depends(get_db)):
    return get_course(db, course_id)

@router.put("/{course_id}", response_model=CourseOut)
def edit_course(course_id: str, data: CourseCreate, db: Session = Depends(get_db)):
    return update_course(db, course_id, data)

@router.delete("/{course_id}")
def remove_course(course_id: str, db: Session = Depends(get_db)):
    delete_course(db, course_id)
    return {"status": "deleted"}
