from queryData import runSelect
from enterData import engine,meta
from interface import getTable , choose

def deleteEntry(table,whereClause):
    #will delete an entry in table, based off of whereClause
    try:
        result=engine.execute(table.delete().where(whereClause))
        print result
    except OperationalError as (statement):
        ePrint(statement,table)
    #need to handle integrity errors
    except:
        print 'fuck: '
        raise
    
def deleteInterface():
    #delete a table entry
    #choose the table to delete an entry from, get the results and display them
    table=getTable()
    results=runSelect(table.c,None)
    x= results.fetchall()
    #provide options to remove all, 1, a rule or none
    s='Table %s has %s entries'%(table,len(x))
    choice=choose(s,['Delete 1 entry',
                   'Delete all entries',
                   'Make a rule to delete by',
                   'Leave it alone'],"Choose an option: ")
    if choice==1:
        #need to whittle down results using searches, must have 1 at the end
        #typing quit exits
        choice1='a'
        while len(x)>1 and choice1<>'quit':
            os='%s options meet the current set of rules'%len(x)
            es="Choose an options(or 'quit'): "
            choice1=choose(os,['Make a rule','Delete all'],es)
        if choice1==1:
            pass
        else:
            pass
        
    elif choice==2:
        pass
    elif choice==3:
        pass
    elif choice==4:
        pass
deleteInterface()
