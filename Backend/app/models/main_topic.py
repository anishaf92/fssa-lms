from sqlalchemy import Column, String, ForeignKey
from app.db.database import Base

class MainTopic(Base):
    __tablename__ = "main_topics"

    main_topic_id = Column(String, primary_key=True)
    course_id = Column(String, ForeignKey("courses.course_id"))
    title = Column(String)
