from flask import Flask, request
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
import random
import re
import math

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'proximity-knighthacks'
app.config['MONGO_URI'] = 'mongodb://grant:chrisisstupid123@ds115045.mlab.com:15045/proximity-knighthacks'

mongo = PyMongo(app)
api = Api(app)

radius = 21
urlRegex = re.compile('https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)')

clientId = random.randint(0,999999)

class Location(Resource):
    def post(self, x, y):
        if not x.isdigit() or not y.isdigit():
            return "Invalid request: invalid coordinates", 400

        locations = mongo.db.locations

        data = request.get_json(force=True)

        if not 'url' in data:
            return "null url", 400

        url = data['url']

        if not urlRegex.match(url):
            return "Invalid request: null url", 400

        location = {'_id': str(x)+','+str(y),
                'url': url}

        locations.insert(location)

    def get(self, x, y):
        if not x.isdigit() or not y.isdigit():
            return "Invalid request: invalid coordinates", 400

        locations = mongo.db.locations
        location = locations.find_one({'_id': str(x)+','+str(y)})

        if location == None:
            return ""

        url = location['url']
        return url

class LocationArea(Resource):
    def get(self, x, y):
        if not x.isdigit() or not y.isdigit():
            return "Invalid request: invalid coordinates", 400

        locations = mongo.db.locations

        grid = {}

        radiusOffset = int(math.ceil(radius/2))

        for ax in range(int(x)-radiusOffset, int(x)+radiusOffset):
            for ay in range(int(y)-radiusOffset, int(y)+radiusOffset):
                location = locations.find_one({'_id': str(ax) + ',' + str(ay)})
                if location != None:
                    if grid[x] == None:
                        grid[x] = {}

                    grid[x][y] = location['url']

        return grid

api.add_resource(Location, '/url/<x>/<y>')
api.add_resource(LocationArea, '/area/<x>/<y>')

if __name__ == '__main__':
    app.run(debug=True)