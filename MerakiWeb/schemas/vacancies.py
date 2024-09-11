from pydantic import BaseModel

class Vacancy(BaseModel):
    id: int
    title: str
    description: str
    requirements: str
    salary: float
    location: str