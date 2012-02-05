#this is used for entering data into our tables

from tableSetup import user,workout,sets,metcon,exercise,meta
from sqlalchemy.orm import mapper
from sqlalchemy.sql import select
from sqlalchemy import create_engine, text

#connect
engine=create_engine('mysql+mysqldb://root:mys3qu3l@localhost/test0',echo=True)
#meta.bind(engine)


def getCols(table):
    ###returns the columns from table in array
    return table.columns

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

    
def runSelect(what,where):
    #executes a select statement with where clause
    #only designed for basics right now
    s=select(what,where)
    results= engine.execute(s)
    return results
    
def selectData():
    #returns an array of entries in table that match whereclause
    sArray=[]       #the array that will hold what we are searching for
    tempArray=[]    # a temporary array holding all column headers in all of our tables
    wheres=[]       #holds the where clause
    #tables=displayArray(meta.sorted_tables,"Pick a table to add to the array(0 to complete)",True) #tables holds all tables being searched
    #[[tempArray.append(thing) for thing in item.c] for item in tables]
    #x=displayArray(tempArray,'Pick items to add to the search list',True)
    #[sArray.append(thing) for thing in x]
    #rule=setWhereClause(tables,tempArray)
    #s=select(sArray,rule)
    tables=meta.sorted_tables[0]
    x=tables.c['uid']
    #rule=setWhereClause(tables,x)
    #print x
    #print rule
    s=select(tables.c,'%s="Charles"'%x)
    print s
    print "++++++++"
    #rule='tables.c["uid"]=="Charles"'
    #s=select(tables.c)
    #s=s.where(tables.c["uid"]=="Charles")
    #print rule
    #s=select(["user.uid, user.pw"],"user.uid='Charles'",from_obj=['user'])
    #print s
    result=engine.execute(s)
    for row in result:
        print row
        #for thing in sArray:
        #    print thing,': ',row[thing]
    #handle this properly!

#runSelect(meta.sorted_tables[0].c,None)
