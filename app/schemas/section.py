from pydantic import BaseModel

# Create
class SectionCreate(BaseModel):
    name: str

# Response
class SectionResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True