from sqlalchemy import Column, String, Integer, ForeignKey
from base import Base


class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address


class Employee(Base):
    __tablename__ = "employes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    position = Column(String)
    company_id = Column(Integer, ForeignKey('companies.id'))

    def __init__(self, name: str, surname: str, position: str, company_id: str):
        self.name = name
        self.surname = surname
        self.position = position
        self.company_id = company_id

