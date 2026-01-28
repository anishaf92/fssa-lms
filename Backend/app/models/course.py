from sqlalchemy import Column, String, ForeignKey
from app.db.database import Base

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(String, primary_key=True)
    course_title = Column(String)
    course_description = Column(String)
    instructor_id = Column(String, ForeignKey("users.user_id"))
    status = Column(String)
