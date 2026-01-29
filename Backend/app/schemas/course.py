from pydantic import BaseModel

class CourseCreate(BaseModel):
    course_id: str
    course_title: str
    course_description: str
    instructor_id: str
    status: str

class CourseOut(CourseCreate):
    model_config = {
        "from_attributes": True
    }
