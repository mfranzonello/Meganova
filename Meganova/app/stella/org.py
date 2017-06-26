'''Customers and companies'''
from typing import List
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,Float,String,JSON,PickleType
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()

class Entity:#(Base):
    #__tablename__ = 'entities'
    #id = Column(Integer,primary_key=True)
    #name = Column(String)
    #type = Column(String)

    def __init__(self,name:str,org_type:str):
        self.name = name
        self.type = org_type
    def __repr__(self):
        return str(self.name)

class IOU(Entity):
    #__tablename__ = 'IOUs'
    #nameplate = Column(Float)
    def __init__(self,name:str,nameplate_multiplier:float=1.0):
        Entity.__init__(self,name,'IOU')
        self.nameplate = nameplate_multiplier

class Provider(Entity):
    #__tablename__ = 'providers'
    #providing = Column(String)
    #associated = Column(String) # ForeignKey?
    def __init__(self,name:str,dacca_type:str,utilites:List[IOU]):
        Entity.__init__(self,name,dacca_type)
        self.providing = dacca_type
        self.associated = utilites

class Direct(Provider):
    def __init__(self,name:str,utilities:List[IOU]):
        Provider.__init__(self,name,'da',utilites)

class CCA(Provider):
    colors = Column(String)

    def __init__(self,name:str,utilities:List[IOU],colors:dict):
        Provider.__init__(self,name,'cca',utilites)
        self.colors = colors

class Customer(Entity):
    def __init__(self,name:str,customer_type:str,zipcode:int):
        if customer_type.lower() in ['school','district','city']:
            self.category = customer_type.lower()
        else:
            self.category = None
        Entity.__init__(self,name,'customer')
        self.zipcode = zipcode
        self.portfolio = None