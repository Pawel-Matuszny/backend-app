from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

import settings
import os

Base=declarative_base()

class App_base(Base):
    __tablename__='app_table'
    ID = Column(Integer,primary_key=True)
    text = Column(String(500))
    status = Column(String(10))
    date_created=Column(DateTime(timezone=True), server_default=func.now())
    is_deleted = Column(String(10),server_default="no")
    def __repr__(self):
        return "<Object number '%d' ('%s', '%s', '%s') is deleted ('%s')> \n" % (self.ID, self.text, self.status,self.date_created, self.is_deleted)
