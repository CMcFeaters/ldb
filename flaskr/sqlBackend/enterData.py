#this is used for entering data into our tables

from tableSetup import user,workout,sets,metcon,exercise,meta
from sqlalchemy.orm import mapper
from sqlalchemy import create_engine
from sqlalchemy.exc import DBAPIError,OperationalError
from sqlalchemy.sql import and_,or_,not_
from datetime import date

#connect
engine=create_engine('sqlite:////Users/Charles/ldb/flaskr/test0.db',echo=True)
meta.bind = engine
#meta.create_all(engine)

def ePrint(statement,table):
    print 'There was an error executing the statement in table %s you sly dog'%table
    print statement[0]	

def getTable():
    #get the table
    choice=-1
    for item in meta.sorted_tables:
        print "%s) %s"%(meta.sorted_tables.index(item),item)
    while range(0,len(meta.sorted_tables)).count(choice)==0:
        choice=int(raw_input('What table would you like to edit: '))
    return meta.sorted_tables[choice]

def createEntry(table,data):
    #will create an entry in table using each item in data{}
    try:
        table.insert().execute(data)
        
    except DBAPIError as (statement):
        ePrint(statement,table)
    #need to handle integrity errors
    except:
        print 'fuck An Error!'
        raise

def enterInterface():
    '''interface for entering data into a table'''
    info=[]
    #get the table
    table=getTable()
    
    print 'Table %s has the following parameters: '%table    
    for col in table.c:
        if col.primary_key==False or str(table)=='user':
            print col.type
            if str(col.type)=="DATE":
                print "Date, using today's until we figure out data validation"
                info.append((col.name,date.today()))
            else:
                info.append((col.name,raw_input('%s: '%col.name)))

    data=dict(info)
    createEntry(table,data)

#deleteEntry(user,"user.uid!='Charles' or user.uid!='Jack'")
