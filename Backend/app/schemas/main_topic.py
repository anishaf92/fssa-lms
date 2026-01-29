from pydantic import BaseModel

class MainTopicCreate(BaseModel):
    main_topic_id: str
    course_id: str
    title: str

class MainTopicOut(MainTopicCreate):
    model_config = {
        "from_attributes": True
    }
