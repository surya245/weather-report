from flask import Flask,jsonify,request
import urllib.request,json
# from pymongo import MongoClient

app = Flask(__name__)

baseAPIURL  = "http://dataservice.accuweather.com"
APIKEY = "2ajULvQ3RuX5CFVYjhCptoYpiG2gMR4O"
locationKeyEP = "/locations/v1/cities/geoposition/search"


sampledict = {'output': 1}
users = {
	'1' : '1',
	'user2' : 'password2',
	'user3' : 'password3',
}

@app.route('/login',methods = ['GET','POST'])
def login():
	#Other options could be to use WTF forms
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if(username in users and users[username] == password):
			## add to db.
			return "logged-in"
		

@app.route('/getWeatherDetails',methods = ['GET','POST'])
def getWeatherdetails():
	if request.method == 'POST':
		username = request.form['user']
		latitude = request.form['lat']
		longitude = request.form['long']

		query = {'user': username,
					 'task': "Get Weather for "
					 		 +latitude+","+longitude
				}
		# parameters = {'apikey' : APIKEY,
		# 			  'q':'12.97,77.58'
		# }
		locationKeyURL = ''.join([baseAPIURL,
								locationKeyEP,
								"?apikey=",
								APIKEY,
								"&q=",latitude,
								"%2C",longitude])

		response = urllib.request.urlopen(locationKeyURL)
		
		dict = json.loads(response.read())
		locationKey = dict["Key"]

		currentConditionsURL = baseAPIURL+"/currentconditions/v1/" + locationKey +"?apikey="+APIKEY
		
		weatherResponse = urllib.request.urlopen(currentConditionsURL)
		## todo add cost by 0.18
		## todo log query to db
		return weatherResponse.read()


@app.route('/home',methods = ['GET'])
def home():
	
	return jsonify(sampledict)

if __name__ == "__main__":
	app.run(debug = True,host = "0.0.0.0", port = 3000)