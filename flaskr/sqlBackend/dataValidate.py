#this is used for entering data into our tables
#used for validating data entered from flaskr
from tableSetup import user,workout,sets, meta
from sqlalchemy.orm import mapper
from sqlalchemy.sql import select
from sqlalchemy import create_engine, text
from queryData import runSelectws
import string

#connect
engine=create_engine('sqlite:////Users/Charles/ldb/flaskr/test0.db',echo=True)
meta.bind=engine

def stringCheck(testString,goodString):
    #verifies testString contains only characters found in good string, returns
    #either '' for a good string or a list of illegal characters
    tArr=[]
    [tArr.append(item.encode("ascii")) for item in testString if goodString.count(item)==0 and tArr.count(item)==0]
    return tArr
    

def uidCheck(nameIn):
    #takes 'nameIn', verifies that is at least 10 characters long
    #contains no characters () and isn't already in use (all lower case)
    #returns a descriptive error or null
    goodString=string.ascii_letters+'0123456789@.-_+'
    res=stringCheck(nameIn,goodString)
    if res!=[]:
        return """The following characters are not allowed: %s"""%res
    elif len(nameIn)<3:
        return 'At least 3 characters'
    elif runSelectws(['user.uid'],'user.uid="%s"'%nameIn)!=[]:
        return 'Username already in use'
    else:
        return ''

def pwCheck(pwIn):
    #takes 'pwIn', verifies that it is at least 10 characters and
    #doesn't contain these cahracters (); returns a descriptive error or null
    goodString=string.ascii_letters+'0123456789@.-_+'
    res=stringCheck(pwIn,goodString)
    
    if res!=[]:
        return """The following characters are not allowed: %s"""%res
    elif len(pwIn)<12:
        return '12 Character minimum'
    else:
        return ''
    

def timeCheck(timeIn):
    #can probably remove this with good website design
    pass

def intCheck(intIn):
    #verifies an int is an int
    #returns null or error
    pass
