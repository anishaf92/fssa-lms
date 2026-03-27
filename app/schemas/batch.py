from pydantic import BaseModel

# Create
class BatchCreate(BaseModel):
    name: str

# Response
class BatchResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True