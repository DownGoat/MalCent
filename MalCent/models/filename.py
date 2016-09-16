__author__ = 'sis13'

from MalCent.database import Model
from sqlalchemy import create_engine, Column, Integer, String, DateTime,\
    ForeignKey, event

class Filename(Model):
    __tablename__ = 'filename'
    id = Column('id', Integer, primary_key=True)
    sample_id = Column(Integer)
    filename = Column(String(256))

    def __init__(self, sample_id=None, filename=None):
        self.sample_id = sample_id
        self.filename = filename
