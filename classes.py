from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Worker(Base):
    __tablename__ = 'worker'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Requester(Base):
    __tablename__ = 'requester'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Qualification(Base):
    __tablename__ = 'qualification'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class UserQualification(Base):
    __tablename__ = 'user_qualification'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    level = Column(Integer)

    qualification_id = Column(Integer, ForeignKey('qualification.id'))
    qualiifcation = relationship(Qualification)


class Dataset(Base):
    __tablename__ = 'dataset'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class DatasetQualifications(Base):
    __tablename__ = 'dataset_qualifications'
    id = Column(Integer, primary_key=True)

    dataset_id = Column(Integer, ForeignKey('dataset.id'))
    dataset = relationship(Dataset)


class DatasetTasks(Base):
    __tablename__ = 'dataset_tasks'
    id = Column(Integer, primary_key=True)

    dataset_id = Column(Integer, ForeignKey('dataset.id'))
    dataset = relationship(Dataset)

    question = Column(String)
    answer = Column(String, nullable=True)
