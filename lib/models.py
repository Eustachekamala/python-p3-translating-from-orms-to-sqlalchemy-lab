#!/usr/bin/env python3

from sqlalchemy import (Column, String, Integer) # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())
    

    def __repr__(self):
        return f'<Dog(name={self.name}, breed={self.breed})>'
