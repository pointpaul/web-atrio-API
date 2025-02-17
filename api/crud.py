from sqlalchemy.orm import Session
from datetime import date, datetime
from . import models, schemas

def get_person(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.id == person_id).first()

def get_persons(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of persons from the database.

    :param db: Session: The database session used to interact with the database.
    :param skip: int: The number of records to skip for pagination.
    :param limit: int: The maximum number of records to return.
    :return: A list of Person objects.
    """
    return db.query(models.Person).order_by(models.Person.last_name).offset(skip).limit(limit).all()

def create_person(db: Session, person: schemas.PersonCreate):
    """
    Create a new person in the database.

    :param db: Session: The database session used to interact with the database.
    :param person: PersonCreate: The schema containing the details of the person to be created.
    :return: The created Person object.
    :raises ValueError: If the person cannot be created due to validation errors.
    """
    age = (datetime.now().date() - person.birth_date).days // 365
    if age >= 150:
        raise ValueError("Person is too old to be registered.")
    db_person = models.Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def create_job_for_person(db: Session, job: schemas.JobCreate, person_id: int):
    """
    Create a new job for a specific person.

    :param db: Session: The database session used to interact with the database.
    :param job: JobCreate: The schema containing the details of the job to be created.
    :param person_id: int: The ID of the person for whom the job is being created.
    :return: The created Job object.
    """
    db_job = models.Job(**job.dict(), person_id=person_id)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_jobs_by_company(db: Session, company_name: str):
    return db.query(models.Job).filter(models.Job.company_name == company_name).all()

def get_persons_by_company(db: Session, company_name: str):
    """
    Retrieve a list of persons who have worked for a specific company.

    :param db: Session: The database session used to interact with the database.
    :param company_name: str: The name of the company to filter persons by.
    :return: A list of Person objects who have worked for the specified company.
    """
    return db.query(models.Person).join(models.Job).filter(models.Job.company_name == company_name).all()

def get_jobs_for_person_between_dates(db: Session, person_id: int, start_date: date, end_date: date):
    """
    Retrieve a list of jobs for a specific person between two dates.

    :param db: Session: The database session used to interact with the database.
    :param person_id: int: The ID of the person whose jobs are being retrieved.
    :param start_date: date: The start date to filter jobs.
    :param end_date: date: The end date to filter jobs.
    :return: A list of Job objects within the specified date range.
    """
    return db.query(models.Job).filter(
        models.Job.person_id == person_id,
        models.Job.start_date >= start_date,
        (models.Job.end_date == None) | (models.Job.end_date <= end_date)
    ).all() 