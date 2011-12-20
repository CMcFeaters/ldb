from __future__ import with_statement
import sys
sys.path.append('C:\\Users\\Charles\\ldb\\flaskr\\sqlBackend')
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
from queryData import runSelectws


DATABASE = '/Users/Charles/ldb/flaskr/test0.db' #where the database we are accessing is stored
#DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME2 = 'admin2'
USERNAME = 'admin'
PASSWORD = 'default'

#create
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS',silent=True)

def connect_db():
    #this is where we would change into our connect code
    #this appears to return a connection
    return sqlite3.connect(app.config['DATABASE'])

'''def init_db():
    #creates database and/or connects to it
    #we will need to change this code so that it executes ldb's db setup script instead
    with closing(connectdb()) as db:
        with app.open_resource('schema.sql') as f: #opens schema.sql file
            db.cursor().executescript(f.read())
        db.commit()
'''

def init_db():
    #creates database and/or connects to it
    #we will need to change this code so that it executes ldb's db setup script instead
    with closing(connectdb()) as db:
        with app.open_resource('schema.sql') as f: #opens schema.sql file
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    #called before a request is made
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    #called after a request is made
    if hasattr(g, 'db'):
        g.db.close()
    
#apparently g is magical and does work behind scenes.  it also
#holds information from one request and is available within each function
'''
@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)'''

@app.route('/')
def show_entries():
    #editing to show entries from liftdb
    if session.get('logged_in'):
        cur = g.db.execute('select uid, pw from user')
        entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]#for row in cur.fetchall()]
    else:
        entries=[]
    return render_template('show_entries.html', entries=entries)
    


@app.route('/add',methods=['POST']) #executes if a post request is made
def add_entry():
    if not session.get('logged_in'):#check for the logged_in key
        abort(401)  #exit if not logged in
    g.db.execute('insert into entries (title,text) values (?,?)',
                 [request.form['title'],request.form['text']])#this is backend code, it inserts into our table
    g.db.commit()   #commit the changes
    flash('New Entry was successfully posted')  #message that gets flashed onthe screen
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])   #routes the login info
def login():
    error = None
    if request.method == 'POST':    #button pressed?
        #check if username is in our database
        if runSelectws(['user.uid'],'user.uid="%s"'%request.form['username']) == []:#run a search here to see if it's in the users.uid table
            error = 'Invalid username'
        elif runSelectws(['user.uid'],'user.uid="%s" and user.pw="%s"'%(request.form['username'],request.form['password'])) ==[]:#run a search here to see if it's in teh users.pw table
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__=='__main__':
    app.run()

