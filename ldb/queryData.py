#this is used for entering data into our tables

from tableSetup import user,workout,sets,metcon,exercise,meta
from sqlalchemy.orm import mapper
from sqlalchemy.sql import Select
from sqlalchemy import create_engine

#connect
engine=create_engine('mysql+mysqldb://root:mys3qu3l@localhost/test0',echo=True)
#meta.bind(engine)


def getCols(table):
    '''returns the columns from table'''
    return table.c





