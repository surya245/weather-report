import json
from urllib import response
import requests
URL = "http://127.0.0.1:3000/"

def home(tries):
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
	if(response.status_code == 500):
		home(tries=tries+1)
	else:
		print(response.text)
		getMenu(username)

def getMenu(username):
	task = '0'
	while(task != '7'):
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

			dict = {"user":username,
					"lat": latitude,
					"long": longitude,
					}

			#add query to db handle from server post.
			response = requests.post(url = URL + '/getWeatherDetails',data= dict)
			print(json.dumps(response.json(),indent = 3))
		# if(task == '2'):
		# 	response = requests.get(url= URL + '/getLastLogin')


if __name__ == "__main__":
	home(0)
