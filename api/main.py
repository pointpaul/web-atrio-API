from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
from typing import List
from datetime import date

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/persons/", response_model=schemas.Person)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new person.

    :param person: PersonCreate: The schema containing the details of the person to be created.
    :param db: Session: The database session dependency.
    :return: The created Person object.
    :raises HTTPException: If the person cannot be created due to validation errors.
    """
    try:
        return crud.create_person(db=db, person=person)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/persons/{person_id}/jobs/", response_model=schemas.Job)
def create_job_for_person(person_id: int, job: schemas.JobCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new job for a specific person.

    :param person_id: int: The ID of the person for whom the job is being created.
    :param job: JobCreate: The schema containing the details of the job to be created.
    :param db: Session: The database session dependency.
    :return: The created Job object.
    """
    return crud.create_job_for_person(db=db, job=job, person_id=person_id)

@app.get("/persons/", response_model=List[schemas.Person])
def read_persons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve a list of persons.

    :param skip: int: The number of records to skip for pagination.
    :param limit: int: The maximum number of records to return.
    :param db: Session: The database session dependency.
    :return: A list of Person objects.
    """
    persons = crud.get_persons(db, skip=skip, limit=limit)
    return persons

@app.get("/companies/{company_name}/persons/", response_model=List[schemas.Person])
def read_persons_by_company(company_name: str, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve a list of persons who have worked for a specific company.

    :param company_name: str: The name of the company to filter persons by.
    :param db: Session: The database session dependency.
    :return: A list of Person objects who have worked for the specified company.
    """
    persons = crud.get_persons_by_company(db, company_name=company_name)
    return persons

@app.get("/persons/{person_id}/jobs/", response_model=List[schemas.Job])
def read_jobs_for_person_between_dates(person_id: int, start_date: date, end_date: date, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve a list of jobs for a specific person between two dates.

    :param person_id: int: The ID of the person whose jobs are being retrieved.
    :param start_date: date: The start date to filter jobs.
    :param end_date: date: The end date to filter jobs.
    :param db: Session: The database session dependency.
    :return: A list of Job objects within the specified date range.
    """
    jobs = crud.get_jobs_for_person_between_dates(db, person_id=person_id, start_date=start_date, end_date=end_date)
    return jobs 