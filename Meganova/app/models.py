"""
Definition of models.
"""
# Django models
from django.db import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey,Column,Integer,String,JSON,PickleType
from sqlalchemy.orm import relationship
import pickle
engine = create_engine('sqlite:///db.sqlite3',echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# import custom code
from app.stella import *

# Meganova models
class IOU(Base):
    __tablename__ = 'IOUs'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    data = Column(PickleType)
    def __init__(self,iou:org.IOU):
        self.name = iou.name
        self.data = pickle.dumps(iou)

class RateDB(Base):
    __tablename__ = 'Rates'
    id = Column(Integer,primary_key=True)
    utility_name = Column(String)
    data = Column(PickleType)
    def __init__(self,rate_db:rates.RatesDB):
        self.utility_name = rates_table.utility.name
        self.data = pickle.dumps(rate_db)

# create engine
Base.metadata.create_all(engine)