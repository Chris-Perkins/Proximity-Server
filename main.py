from flask import Flask, request
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
import random

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'proximity-knighthacks'
app.config['MONGO_URI'] = 'mongodb://grant:chrisisstupid123@ds115045.mlab.com:15045/proximity-knighthacks'

mongo = PyMongo(app)
api = Api(app)

clientId = random.randint(0,999999)

class Location(Resource):
    def post(self, x, y):
        if not x.isDigit() and not y.isDigit():
            return {
                "invalid coordinates"
            }, 400

        locations = mongo.db.locations

        data = request.get_json(force=True)

        location = {'_id': str(x)+','+str(y),
                'url': data['url']}

        locations.insert(location)

    def get(self, x, y):
        if not x.isDigit() and not y.isDigit():
            return {
                "invalid coordinates"
            }, 400

        locations = mongo.db.locations
        location = locations.find_one({'_id': str(x)+','+str(y)})
        url = location['url']
        return url


api.add_resource(Location, '/<x>/<y>')

if __name__ == '__main__':
    app.run(debug=True)