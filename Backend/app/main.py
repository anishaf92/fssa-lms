from fastapi import FastAPI
from app.db.database import Base, engine
from app.router import user, course, main_topic, sub_topic, content

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FSSA LMS Backend")

app.include_router(user.router)
app.include_router(course.router)
app.include_router(main_topic.router)
app.include_router(sub_topic.router)
app.include_router(content.router)

@app.get("/")
def health():
    return {"Message" : "App Health is Good "}