'''this process clears all of the old tables and creates new blank tables'''
#this creates our test tables
from tableSetup import sets,lifts,workout,user,meta
from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
#from test0Classes import User,Workout,Lifts,Sets,Metcon,Exercise

#mys_engine=create_engine('mysql+mysqldb://root:mys3qu3l@localhost/test0',echo=True)
'''this will create our engine.  i'm bad with this point, but the engine handles our connection and requests to the
database.  we create it once and then use it to add, drop, connect, and execute commands to and from teh database.
Consider it as if the database hates you, but likes engine, so you have to go through engine to get what you need
from teh database'''
mys_engine=create_engine('sqlite:////Users/Charles/ldb/flaskr/test0.db',echo=True)

'''here we drop all of our old tables.  we do this because create all (used below) does not create new tables if
that same table already exists'''
sets.drop(mys_engine,checkfirst=True)  
lifts.drop(mys_engine,checkfirst=True)
workout.drop(mys_engine,checkfirst=True)
user.drop(mys_engine,checkfirst=True)
 


'''this was the old function we used: meta.create_all(mys_engine)
this is stupid.  we didn't bind metadata and then used mys_engine in the bind parameter spot.
Although I don't know the pro's and con's of binding, we are going to bind then create - Project king'''

meta.bind=mys_engine '''mys_engine is now bound to our metadata'''
meta.create_all()       '''this creates all the tables that make up our metadata object'''

'''if we have bound our metadata to an engine, we can do connectionless queries from our table ojbects
        i.e. res=user.select().execute()'''

'''unbound this would look like:
    connection=engine.connect()
    res=connection.execute(user.select())'''

'''binding is quicker and i'm sure there are horrible downsides, but fuck it - Project King'''
 








