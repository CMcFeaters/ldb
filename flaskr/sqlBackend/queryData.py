#this is used for entering data into our tables

from tableSetup import user,workout,sets,meta
from sqlalchemy.orm import mapper
from sqlalchemy.sql import select
from sqlalchemy import create_engine, text

#connect
engine=create_engine('sqlite:////Users/Charles/ldb/flaskr/test0.db',echo=True)
meta.bind=engine '''We just bound to the engine, now we can access all database functions
using table.blahblahblah'''

#NOTE, most of these functions are ugly and meant to be text based
    #we then morphed them to be used by the browser/FLASK PROGRAM
    #this is wrong.  These will be either marked text or re-written
    #directly for use by FLASKR
    '''this whole section will be re-written'''

    

