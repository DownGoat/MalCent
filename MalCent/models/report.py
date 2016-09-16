

__author__ = 'sis13'

from MalCent.database import Model
from sqlalchemy import create_engine, Column, Integer, String, DateTime,\
    ForeignKey, event

class Report(Model):
    __tablename__ = 'report'
    id = Column('id', Integer, primary_key=True)
    sha1 = Column(String(40))
    sha256 = Column(String(64))
    md5 = Column(String(32))
    ssdeep = Column(String(512))
    filesize = Column(Integer)
    first_seen = Column(DateTime(timezone=True))
    last_seen = Column(DateTime(timezone=True))

    def __init__(self, sha1=None, sha256=None, md5=None, ssdeep=None, last_seen=None, first_seen=None, filesize=None):
        self.sha1 = sha1
        self.sha256 = sha256
        self.md5 = md5
        self.ssdeep = ssdeep
        self.last_seen = last_seen
        self.first_seen = first_seen
        self.filesize = filesize
