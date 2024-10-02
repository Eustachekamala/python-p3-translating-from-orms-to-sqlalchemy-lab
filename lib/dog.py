from models import Dog
from sqlalchemy.orm import Session # type: ignore

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session:Session, dog:Dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session:Session, name:str):
    return session.query(Dog).filter(Dog.name == name).first()
    
def find_by_id(session:Session, id:int):
    return session.query(Dog).filter(Dog.id == id).first()
    
def find_by_name_and_breed(session:Session, name:str, breed:str):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    session.query(Dog).filter(Dog.id == dog.id).update({'breed': breed})
    session.commit()