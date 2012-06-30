#this is used for entering data into our tables

from tableSetup import user,workout,sets,meta
from sqlalchemy.orm import mapper
from sqlalchemy import create_engine
from sqlalchemy.exc import DBAPIError,OperationalError
from sqlalchemy.sql import and_,or_,not_
from datetime import date

#connect
engine=create_engine('sqlite:////Users/Charles/ldb/flaskr/test0.db',echo=True)
meta.bind = engine '''We just bound to the engine, now we can access all database functions
using table.blahblahblah'''

def ePrint(statement,table):
    '''this is just an error statement, it prints out the table the error was in and
    the particular error statement'''
    print 'There was an error executing the statement in table %s you sly dog'%table
    print statement[0]	

#NOTE, most of these functions are ugly and meant to be text based
    #we then morphed them to be used by the browser/FLASK PROGRAM
    #this is wrong.  These will be either marked text or re-written
    #directly for use by FLASKR

def getTable():
    '''text'''
    #get the table
    choice=-1
    for item in meta.sorted_tables:
        print "%s) %s"%(meta.sorted_tables.index(item),item)
    while range(0,len(meta.sorted_tables)).count(choice)==0:
        choice=int(raw_input('What table would you like to edit: '))
    return meta.sorted_tables[choice]

def enterInterface():
    '''interface for entering data into a table'''
    '''TEXT'''
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

'''FLASKR FUNCTIONS'''

def createEntry(table,data):
    '''given meta data object table, will write all data to the table unless there is an error'''
    try:
        table.insert().execute(data)'''attempt insertion'''
        
    except DBAPIError as (statement):   '''this is an error we could get from sqlalchemy, it is the whole subclass of errors'''
        ePrint(statement,table)
    #need to handle integrity errors
    except:         '''a different error that is not part of sqlalchemy base class'''
        print 'fuck An Error!'
        raise

#deleteEntry(user,"user.uid!='Charles' or user.uid!='Jack'")
