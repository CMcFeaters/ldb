#this is used for entering data into our tables

from tableSetup import user,workout,sets,metcon,exercise,meta
from sqlalchemy.orm import mapper
from sqlalchemy import create_engine
from sqlalchemy.exc import DBAPIError,OperationalError
from sqlalchemy.sql import and_,or_,not_

#connect
engine=create_engine('mysql+mysqldb://root:mys3qu3l@localhost/test0',echo=True)
meta.bind = engine
#meta.create_all(engine)

def ePrint(statement,table):
    print 'There was an error executing the statement in table %s you sly dog'%table
    print statement[0]	

def deleteEntry(table,whereClause):
    #will delete an entry in table, based off of whereClause
    try:
        result=engine.execute(table.delete().where(whereClause))
        print result
    except OperationalError as (statement):
        ePrint(statement,table)
        
    except:
        print 'fuck: '
        raise

def createEntry(table,data):
    #will create an entry in table using each item in data{}
    try:
        
        table.insert().execute(data)
        
    except DBAPIError as (statement):
        ePrint(statement,table)
 
    except:
        print 'fuck:'
        raise


#deleteEntry(user,"or_(user.uid!='Charles',user.uid!='Jack')")
