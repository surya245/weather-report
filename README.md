# weather-report
Get weather report by geolocation

A commandline client-server app to get weather report and user-activity info on the portal.

On Successful Login, User can Get weather details based on Geo-location.
Weather details are taken from http://www.7timer.info/

# Tech Used : Python Flask, Docker, MongoDB

# Setup and Run
1. Install Python 3.10.
2. Install Docker.
3. Clone the repository.
4. Run the server and Web.
	```docker compose up web mongo```
5. Run the client.
	```docker compose run client```
	Instructions in the client app are self-explainatory.
6. Remove containers.
	```docker compose down```


Resources Referred:
https://code.visualstudio.com/docs/python/tutorial-flask
https://www.geeksforgeeks.org/get-post-requests-using-python/
https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
https://datagy.io/python-requests-post/
https://github.com/Yeqzids/7timer-issues/wiki/Wiki
http://www.7timer.info/doc.php?lang=en
https://www.section.io/engineering-education/integrating-external-apis-with-flask/
https://www.mongodb.com/languages/python
https://www.w3schools.com/python/python_mongodb_getstarted.as
https://medium.com/analytics-vidhya/creating-dockerized-flask-mongodb-application-20ccde391ap
https://www.mongodb.com/languages/python
https://hub.docker.com/_/mongo
https://www.prisma.io/dataguide/mongodb/setting-up-a-local-mongodb-database
https://www.prisma.io/dataguide/mongodb/connecting-to-mongodb
https://stackoverflow.com/questions/71039178/how-to-connect-flask-app-to-mongodb-with-docker-compose
https://docs.docker.com/engine/reference/builder/
https://docs.docker.com/compose/compose-file/
https://docs.docker.com/compose/reference/
https://docs.docker.com/engine/reference/commandline/compose/
https://stackoverflow.com/questions/18473409/how-to-persist-mongodb-data-between-container-restarts