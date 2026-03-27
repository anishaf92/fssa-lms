from pydantic import BaseModel

# Create
class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

# Response
class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int

    class Config:
        from_attributes = True