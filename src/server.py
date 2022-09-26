from crypt import methods
import re
from sys import base_prefix
from xmlrpc.client import DateTime
from flask import Flask,jsonify,request
import urllib.request,json
import db

app = Flask(__name__)

BASE_PREFIX= "http://www.7timer.info/bin/api.pl?"
BASE_SUFFIX = "&product=astro&output=json"

USERS = {
	'user1' : '1',
	'user2' : 'password2',
	'user3' : 'password3',
}

'''
Endpoint: '/'

params: None

root directory,initializes Database

returns: Prompt on successful connections
'''
@app.route('/',methods = ['GET'])
def root():
	db.init_db()
	return "Connection Succesfull!!"

'''
EndPoint: /login

params: Username,
		Password

Checks for user Authentication,
Calls db for last login and login History Update

returns: Success Message or HTTP Error code
'''
@app.route('/login',methods = ['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if(username in USERS and USERS[username] == password):
			db.update('Login',username)
			return "Log-in Successful!!!\n"
	response = app.response_class(status = 401)
	return response

'''
EndPoint: '/weatherDetails'

params: username,
		geo-coordinates

Connnects to 7timer, weather API, fetches Weather details,
Updates bill for the user and stores the query in DB.

returns: Weather Details or HTTP Error code
'''
@app.route('/weatherDetails',methods = ['GET','POST'])
def weatherdetails():
	if request.method == 'POST':
		username = request.form['user']
		latitude = request.form['lat']
		longitude = request.form['long']
		query = ''.join(['Get Weather for ',
					 		 latitude,
							 ",",
							 longitude])
		
		
		fullURL = ''.join([BASE_PREFIX,
						 "lon=",longitude,
						 "&lat=",latitude,
						 BASE_SUFFIX])
		weatherResponse = urllib.request.urlopen(fullURL)
		
		
		db.update('Query',username,query,cost=0.18)

		return weatherResponse.read()

'''
EndPoint: '/lastLogin',

params: username

Gets last login time from user,
Updates the query log for user.

returns : Previous Login Details.
'''
@app.route('/lastLogin',methods = ['GET','POST'])
def lastLogin():
	if request.method == 'POST':
		username = request.form['user']
		record = db.query(username)
		query = 'Get Last Login Detail'
		db.update('Query',username,query)
		return jsonify(record['loginHistory'][-2])

'''
EndPoint: '/loginHistory',

params: username,

Gets Login History from database,
Updates the query log for user.

returns: List of login history.
'''
@app.route('/loginHistory',methods = ['GET','POST'])
def loginHistory():
	if request.method == 'POST':
		username = request.form['user']
		record = db.query(username)
		query = 'Get Login History'
		db.update('Query',username,query)
		return jsonify(record['loginHistory'])

'''
EndPoint: '/allUsers',

params: username,

Gets list of user from dict,
Updates the query log for user.

returns: List containing all userIds.
'''
@app.route('/allUsers',methods = ['GET','POST'])
def allUsers():
	if request.method == 'POST':
		username = request.form['user']
		query = 'Get Users List'
		db.update('Query',username,query)
	return jsonify(list(USERS.keys()))

'''
EndPoint: '/bill',

params: username,

Fetches the current cost from DB,
Updates query log for user.

returns: Current Bill amount.
'''
@app.route('/bill',methods = ['GET','POST'])
def bill():
	if request.method == 'POST':
		username = request.form['user']
		query = 'Get Bill'
		db.update('Query',username,query)
		record = db.query(username)
		return jsonify(record['currentBill'])

'''
EndPoint: '/allQueries'

params: username,

Gets the query log from DB.
Add current query to the logs.

returns: list of all previous query.
'''
@app.route('/allQueries',methods = ['GET','POST'])
def allQueries():
	if request.method == 'POST':
		username = request.form['user']
		record = db.query(username)
		query = 'Get All Previous Queries'
		db.update('Query',username,query)
		return jsonify(record['query'])


'''
main:

Initiates flask application,
'''
if __name__ == "__main__":
	#db.cleanUp()
	app.run()