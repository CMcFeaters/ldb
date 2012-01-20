#this is used for entering data into our tables

from tableSetup import user,workout,sets,metcon,exercise,meta
from sqlalchemy.orm import mapper
from sqlalchemy.sql import select
from sqlalchemy import create_engine, text

#connect
engine=create_engine('sqlite:////Users/Charles/ldb/flaskr/test0.db',echo=True)
meta.bind=engine

def setWhereClause(tables,cols):
    ###sets the whereclause for a select, cols is an array of column between tables being searched for, tables contains the tables being
    s='Select the term to search by'
    whereArray=[]
    #char=displayArray(cols,s,False)
    char=cols
    print 'Assigning rule to ',char
    rule=raw_input('where %s is: '%char)
    rule=char+rule
    print rule
    print 
    return rule    
    
def setSearchArray(tables):
    ###returns an array containing the items searched for
    searchArray=[]
    #choose a table and add items to that tables array
    #repeat until 0 is selected
    s='Select a table to choose columns from'
    x=displayArray(tables,s,False)
    while x!='*':
        searchArray.append(displayArray(x[0].c,'Select the items to display',True))
        x=displayArray(tables,'Select a table to choose columns from',False)
    
    print searchArray        

def displayArray(arr,searchMessage,multi):
    ###numerically displays an array, 0 returns all selected things, multi signifies whether 1 or mutliple
    ###things are able to be selected
    searchArray=[]
    found=False
    choice=-1
    #display list
    for item in arr:
        print "%s) %s"%(arr.index(item)+1,item)
    #make choices, varies if multiple or single entries are required
    while (multi and choice!=0) or (not multi and not found):
        choice=raw_input(searchMessage+': ')

        #make sure they didn't input a fucking non-number
        if choice.isdigit():
            choice=int(choice)

            #make sure it's in the list and add it to the array
            if range(0,len(arr)).count(choice-1)>0:
                if searchArray.count(arr[choice-1])==0:
                    searchArray.append(arr[choice-1])
                    found=True

    #if they didn't choose anything
    if len(searchArray)==0:
        return ['*']
    else:
        return searchArray

    
def runSelectws(what,where):#wherec,wheres):
    #executes a select statement with where clause
    #what is an array of strings for the columns being returned form: table.col
    #where is a wherestatement string
    carr=[]
    warr=[]
    for item in what:
        r=str(item).split('.')
        carr.append(meta.tables[r[0]].c[r[1]])
    s=select(carr,where)
    results= engine.execute(s)
    
    return results.fetchall()

def search(what,where):
    #search function, given what you want to search for and a where result
    pass

def quickSearch():
    #displays all entries in a table selected by
    tbl= list(meta.tables)
    arr=displayArray(tbl,'Pick your table',False)
    print runSelectws(meta.tables[arr[0]].c,'')
    

