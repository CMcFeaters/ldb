from enterData import deleteEntry,createEntry,engine,meta

def getTable():
    #get the table
    choice=-1
    for item in meta.sorted_tables:
        print "%s) %s"%(meta.sorted_tables.index(item),item)
    while range(0,len(meta.sorted_tables)).count(choice)==0:
        choice=int(raw_input('What table would you like to edit: '))
    return meta.sorted_tables[choice]

def enterInterface():
    '''interface for entering data into a table'''
    info=[]
    #get the table
    table=getTable()
    
    for col in table.c:
        if col.primary_key==False or str(table)=='user':
            info.append((col.name,raw_input('%s: '%col.name)))

    data=dict(info)
    createEntry(table,data)

def deleteInterface():
    '''interface for delete data from a table'''
    info=[]
    table=getTable()

    print 'Table %s has the following parameters: '%table

enterInterface()
