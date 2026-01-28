from pydantic import BaseModel

class ContentCreate(BaseModel):
    content_id: str
    sub_topic_id: str
    content_type: str
    title: str
    content_url: str

class ContentOut(ContentCreate):
    model_config = {
        "from_attributes": True
    }
