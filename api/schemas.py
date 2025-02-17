from typing import List, Optional
from pydantic import BaseModel
from datetime import date

class JobBase(BaseModel):
    company_name: str
    position: str
    start_date: date
    end_date: Optional[date] = None

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    person_id: int

    class Config:
        orm_mode = True

class PersonBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    id: int
    jobs: List[Job] = []

    class Config:
        orm_mode = True 