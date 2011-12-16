from __future__ import with_statement
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing


DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
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

def init_db():
    #creates database and/or connects to it
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
    g.db.close()
    
#apparently g is fucking magical and does work behind scenes.  it also
#holds information from one request and is available within each function

@app.route('/add',methods=['POST']) #executes if a post request is made
def add_entry():
    if not session.get('logged_in'):#check for the logged_in key
        abort(401)  #exit if not logged in
    g.db.execute('insert into entries (title,text) values (?,?)',
                 [request.form['title'],request.form['text']])
    g.db.commit()   #commit the changes
    flash('New Entry was successfully posted')  #message that gets flashed onthe screen
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
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

