#this is used for entering data into our tables

from tableSetup import user,workout,sets,metcon,exercise,meta
#from tableSetup import User,Workout,Lifts,Sets,Metcon,Exercise,lifts
from sqlalchemy.orm import mapper
from sqlalchemy.sql import Select

#connect
engine=create_engine('mysql+mysqldb://root:mys3qu3l@localhost/test0',echo=True)
meta.bind(engine)


