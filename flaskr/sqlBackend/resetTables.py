'''this is our new setup for the fitness charts using sql alchemy'''
#this creates our test tables
from tableSetup import sets,lifts,exercise,metcon,workout,user,meta
from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
#from test0Classes import User,Workout,Lifts,Sets,Metcon,Exercise

#mys_engine=create_engine('mysql+mysqldb://root:mys3qu3l@localhost/test0',echo=True)
mys_engine=create_engine('sqlite:////Users/Charles/ldb/flaskr/test0.db',echo=True)

sets.drop(mys_engine,checkfirst=True)
lifts.drop(mys_engine,checkfirst=True)
exercise.drop(mys_engine,checkfirst=True)
metcon.drop(mys_engine,checkfirst=True)
workout.drop(mys_engine,checkfirst=True)
user.drop(mys_engine,checkfirst=True)


meta.create_all(mys_engine)







