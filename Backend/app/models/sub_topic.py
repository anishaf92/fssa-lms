from sqlalchemy import Column, String, ForeignKey
from app.db.database import Base

class SubTopic(Base):
    __tablename__ = "sub_topics"

    sub_topic_id = Column(String, primary_key=True)
    main_topic_id = Column(String, ForeignKey("main_topics.main_topic_id"))
    title = Column(String)
