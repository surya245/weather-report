from datetime import datetime
from pymongo import MongoClient
import server

DB_CLIENT = MongoClient(host= 'database',
					   port = 27017)
DATABASE = DB_CLIENT["user_activity_db"]
ACTIVITY = DATABASE['activity']

'''
Updates DB with new users1,
Initializes on first run.
'''
def init_db():
	listOfUsers = []
	for x in ACTIVITY.find():
			listOfUsers.append(x['_id'])
	for user in server.USERS:
		if not user in listOfUsers:
			activityRecord = {
				'_id' : user,
				'lastLogin' : datetime.now(),
				'loginHistory' : [datetime.now()],
				'query':[],
				'currentBill': 0
			}
			ACTIVITY.insert_one(activityRecord)
	return
'''
Updates the Database based on type.
'''
def update(updateType,user,userQuery='',cost = 0):
	
	dbQuery = {'_id': user}
	userRecord = ACTIVITY.find(dbQuery)
	
	userCurrentBill = 0
	lastLogin = datetime.now()

	'''
	Get the record for user.

	'''
	for record in userRecord:
		userLoginHistory = record['loginHistory']
		userLoginHistory.append(lastLogin)
		
		existingQuery = record['query']
		existingQuery.append(userQuery)

		userCurrentBill = record['currentBill']
	'''
	If called from Login API,
		Updates lastLogin and History Details.
	Otherwise,
		Updates the query and cost for query.
	'''
	if(updateType == 'Login'):
		ACTIVITY.update_one(dbQuery,
									{
										'$set': {'lastLogin':lastLogin,
												 'loginHistory':userLoginHistory
												 }
									})
	elif updateType == 'Query':
		userCurrentBill += cost
		ACTIVITY.update_one(dbQuery,
									{
										'$set': {'query' : existingQuery,
												 'currentBill':userCurrentBill}
									})
	userRecord = ACTIVITY.find(dbQuery)
	for record in userRecord:
		print(record)

'''
Get record Based on username(Index)
'''
def query(user):
	dbQuery = {'_id': user}
	userRecord = ACTIVITY.find(dbQuery)
	for record in userRecord:
		if(record['_id'] == user):
			return record

'''
Clears all records.
'''
def cleanUp():
	for user in server.USERS.keys():
		ACTIVITY.delete_one({'_id':user})

'''
Used to create fresh db for testing
'''
if __name__ == "__main__":
	cleanUp()
	init_db()

