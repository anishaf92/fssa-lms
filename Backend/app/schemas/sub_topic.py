from pydantic import BaseModel

class SubTopicCreate(BaseModel):
    sub_topic_id: str
    main_topic_id: str
    title: str

class SubTopicOut(SubTopicCreate):
    model_config = {
        "from_attributes": True
    }
