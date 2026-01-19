from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FSSA-LMS backend running"}
