import json
from urllib import response
import requests
URL = "http://weather-report:3000"
#URL = "http://172.17.0.2:3000"

'''
checkConnection:

params: None

Contacts Weather Apps root directory,
Moves to login if connection is successful.

returns: Response recieved, error code on Failue.
'''
def checkConnection():
	response = requests.get(url=URL+"/")
	if(response.status_code == 200):
		print(response.text)
		login(0)
	else :
		print(response.status_code)

'''
login:

params: Count of Attempts.

Sends login credentials to the server,
Provides 3 retries on wrong credentials,
Displays App Menu on successful login

returns: Error code on server errors.
'''
def login(tries):
	if(tries > 3):
		print("No more attempts left")
		return
	if(tries != 0):
		print("Retry logging in")
	else:
		print("Login with your credentials")
	username = input("Username:")
	password = input("Password:")
	dict = {'username': username, 'password': password}
	response = requests.post(url= URL + "/login",data = dict)
	if(response.status_code != 200):
		print(response.text)
		login(tries=tries+1)
	else:
		print(response.text)
		getMenu(username)

'''
getMenu:

params: username - id for current user.

Displays Menu of App till Exit command is given,
Connects with different endpoints on the server
based on request and fetches the appropriate response
or error codes.

returns: None
'''
def getMenu(username):
	task = '0'
	while(task != '7'):
		dict = {"user":username}
		print('''What Do you want to do?
	1. Get Weather details
	2. Last login
	3. Login history
	4. List of All Users
	5. Get Bill
	6. List all previous query
	7. Quit Application\n''')
		
		task = input("Enter number\n")
		if task == '1':
			latitude = input("Enter Latitude: ")
			longitude = input("Enter Longitude: ")

			newdict = {
				"lat": latitude,
				"long": longitude,
				}
			newdict.update(dict)
			response = requests.post(url = URL + '/weatherDetails',data= newdict)
			if(response.status_code == 200):
				print(json.dumps(response.json(),indent = 3))
			else :
				print(response.status_code)
			carryOn = input("Anything else?(y/n)")
			if(carryOn == 'n'):
				print("See You Later!!!")
				task = '7'

		elif task == '2':
			response = requests.post(url= URL + '/lastLogin',data= dict)
			if(response.status_code == 200):
				print(response.text)
			else :
				print(response.status_code)
			carryOn = input("Anything else?(y/n)")
			if(carryOn == 'n'):
				print("See You Later!!!")
				task = '7'

		elif task == '3':
			response = requests.post(url= URL + '/loginHistory',data= dict)
			if(response.status_code == 200):
				print(response.text)
			else :
				print(response.status_code)
			carryOn = input("Anything else?(y/n)")
			if(carryOn == 'n'):
				print("See You Later!!!")
				task = '7'

		elif task == '4':
			response = requests.post(url = URL + '/allUsers',data=dict)
			if(response.status_code == 200):
				print(response.text)
			else :
				print(response.status_code)
			carryOn = input("Anything else?(y/n)")
			if(carryOn == 'n'):
				print("See You Later!!!")
				task = '7'

		elif task == '5':
			response = requests.post(url = URL + '/bill',data=dict)
			
			if(response.status_code == 200):
				print("$"+response.text)
			else :
				print(response.status_code)
			carryOn = input("Anything else?(y/n)")
			if(carryOn == 'n'):
				print("See You Later!!!")
				task = '7'
		
		elif task == '6':
			response = requests.post(url= URL + '/allQueries',data = dict)
			if(response.status_code == 200):
				print(response.text)
			else :
				print(response.status_code)
			carryOn = input("Anything else?(y/n)")
			if(carryOn == 'n'):
				print("See You Later!!!")
				task = '7'
		elif task != '7':
			print("Wrong Input!!")
		else:
			print("See You Later!!!")


'''
Main Execution for client.
'''
if __name__ == "__main__":
	checkConnection()
	
