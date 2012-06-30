from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine,Table,Column,Integer,String,ForeignKey,Date,Time, MetaData

'''all that happens in this function is we define our table objects, assign them to our metadata object and
create the classes that represent our tables.'''

meta=MetaData() '''meta will hold our metadata, metadata is a collection of table objects
                is an instance of a metadata object'''

class User(object):
    def __init__(self,uid,name,pw):
        self.uid=uid
        self.name=name
        self.pw=pw

class Workout(object):
    def __init__(self,wdate,wstatus):
        self.wdate=wdate
        self.wstatus=wstatus

class Lifts(object):
    def __init__(self,ltype,units):
        self.ltype=ltype
        self.units=units

class Sets(object):
    def __init__(self,reps,weight):
        self.reps=reps
        self.weight=weight

user=Table('user',meta,
           Column('uid',String(20),primary_key=True),
           Column('name',String(20)),
           Column('pw',String(20))
           )
'''user is a table object, this table has the properties/types shown above and is part of our metadata object meta'''

workout=Table('workout',meta,
              Column('wid',Integer,primary_key=True),
              Column('uid',String(20),ForeignKey('user.uid')),
              Column('wdate',Date),
              Column('wstatus',String(51)),
              )

lifts=Table('lifts',meta,
           Column('wid',ForeignKey('workout.wid')),
           Column('lid',Integer,primary_key=True),
           Column('ltype',String(20)),
           Column('units',String(10))
           )

sets=Table('sets',meta,
          Column('sid',Integer,primary_key=True),
          Column('lid',Integer,ForeignKey('lifts.lid')),
          Column('reps',Integer),
          Column('weight',Integer))

