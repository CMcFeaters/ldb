from queryData import quickSearch
from enterData import engine,meta, enterInterface

def getTable():
    #get the table
    choice=-1
    for item in meta.sorted_tables:
        print "%s) %s"%(meta.sorted_tables.index(item),item)
    while range(0,len(meta.sorted_tables)).count(choice)==0:
        choice=int(raw_input('What table would you like to edit: '))
    return meta.sorted_tables[choice]


def choose(os,arr,es):
    #a quick function to display our text menus
    #takes in an array of text options returns a decimal representing the
    #corresponding choice
    choice=-1
    #print arr
    while range(1,len(arr)+1).count(choice)==0 and choice!='quit'.lower():
        print os
        for item in arr:
            print '%s) %s'%(arr.index(item)+1,item)
        choice=raw_input(es)
        if choice.isdigit():
            choice=int(choice)
    return choice

enterInterface()
#quickSearch()

