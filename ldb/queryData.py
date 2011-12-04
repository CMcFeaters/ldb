#this is used for entering data into our tables

from tableSetup import user,workout,sets,metcon,exercise,meta
from sqlalchemy.orm import mapper
from sqlalchemy.sql import select
from sqlalchemy import create_engine

#connect
engine=create_engine('mysql+mysqldb://root:mys3qu3l@localhost/test0',echo=True)
#meta.bind(engine)


def getCols(table):
    ###returns the columns from table in array
    return table.columns

def setWhereClause(tables,columns):
    ###sets the whereclause for a select
    pass
        
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

'''def setColumnArray(tables):
    #sets the columns being returned for a select statement
    #for table in tables:
    #    for col in table.c:
    common=[]
    x=[[col.name for col in table.c] for table in tables]
    for item in x[0]:
        flag=True
        for arr in x:
            if arr.count(item)==0: flag=False
        if flag: common.append(item)
    return common'''

        
'''def setTableArray():
    #sets the tables being searched in a select statement
    choice=-1
    table_array=[]
    for item in meta.sorted_tables:
        print "%s) %s"%(meta.sorted_tables.index(item)+1,item)
    while choice!=0:
        choice=int(raw_input('Pick a table to add to the array(0 to complete): '))
        if range(0,len(meta.sorted_tables)).count(choice-1)>0:
            if table_array.count(meta.sorted_tables[choice-1])==0:
                table_array.append(meta.sorted_tables[choice-1])
    if len(table_array)==0:
        return meta.sorted_tables
    else:
        return table_array'''
        

def selectData():
    #returns an array of entries in table that match whereclause
    sArray=[]
    tempArray=[]
    tables=displayArray(meta.sorted_tables,"Pick a table to add to the array(0 to complete)",True)
    for item in tables:
        [tempArray.append(thing) for thing in item.c]
        x=displayArray(tempArray,'Pick items to add to the search list',True)
        [sArray.append(thing) for thing in x]

    s=select(sArray)
    result=engine.execute(s)
    for row in result:
        for thing in sArray:
            print thing,': ',row[thing]
    #handle this properly!

selectData()
