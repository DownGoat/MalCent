__author__ = 'sis13'

from MalCent.database import Model
from sqlalchemy import create_engine, Column, Integer, String, DateTime,\
    ForeignKey, event

class Queue(Model):
    __tablename__ = 'queue'
    id = Column('id', Integer, primary_key=True)
    sha1 = Column(String(40))
    filename = Column(String(256))
    filesize = Column(Integer)

    def __init__(self, sha1=None, filename=None, filesize=None):
        self.sha1 = sha1
        self.filename = filename
        self.filesize = filesize
