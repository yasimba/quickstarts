from flask import Flask
from flask_restful import Api
from resources.resource import Resource


app = Flask(__name__)
api = Api(app)

api.add_resource(Resource, '/Resource')
