from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    status = Column(String, nullable=False)

    batch_id = Column(Integer, ForeignKey("batches.id"))
    section_id = Column(Integer, ForeignKey("sections.id"))

    batch = relationship("Batch", back_populates="students")
    section = relationship("Section", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")