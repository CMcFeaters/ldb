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



def createEntry(table,data):
    #will create an entry in table using each item in data{}
    try:
        table.insert().execute(data)
        
    except DBAPIError as (statement):
        ePrint(statement,table)
    #need to handle integrity errors
    except:
        print 'fuck:'
        raise
    
def enterInterface():
    '''interface for entering data into a table'''
    info=[]
    #get the table
    table=getTable()

    print 'Table %s has the following parameters: '%table    
    for col in table.c:
        if col.primary_key==False or str(table)=='user':
            info.append((col.name,raw_input('%s: '%col.name)))

    data=dict(info)
    createEntry(table,data)

#deleteEntry(user,"user.uid!='Charles' or user.uid!='Jack'")
