from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine,Table,Column,Integer,String,ForeignKey,Date,Time, MetaData

meta=MetaData()

class User(object):
    def __init__(self,uid,pw):
        self.uid=uid
        self.pw=pw

class Workout(object):
    def __init__(self,wtime,wdate,wstatus):
        self.wtime=wtime
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

class Metcon(object):
    def __init__(self,rounds,mTime,mScore):
        self.rounds=rounds
        self.mTime=mTime
        self.mScore=mScore

class Exercise(object):
    def __init__(self,movement,weight,distance,reps):
        self.movement=movement
        self.distance=distance
        self.weight=weight
        self.reps=reps

user=Table('user',meta,
           Column('uid',String(20),primary_key=True),
           Column('pw',String(20))
           )

workout=Table('workout',meta,
              Column('wid',Integer,primary_key=True),
              Column('uid',String(20),ForeignKey('user.uid')),
              Column('wtime',Time),
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

metcon=Table('metcon',meta,
             Column('wid',Integer,ForeignKey('workout.wid')),
             Column('mid',Integer,primary_key=True),
             Column('rounds',Integer),
             Column('mTime',Time),
             Column('mScore',Integer)
             )

exercise=Table('exercise',meta,
               Column('eid',Integer,primary_key=True),
               Column('mid',Integer,ForeignKey('metcon.mid')),
               Column('movement',String(20)),
               Column('weight',Integer),
               Column('distance',Integer),
               Column('reps',Integer)
               )