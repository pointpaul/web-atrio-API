from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    birth_date = Column(Date)

    jobs = relationship("Job", back_populates="person")

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    position = Column(String)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    person_id = Column(Integer, ForeignKey("persons.id"))

    person = relationship("Person", back_populates="jobs") 