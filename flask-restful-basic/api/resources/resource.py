from flask_restful import Resource

class Resource(Resource):
    def get(self):
        return {'hello': 'world'}
    
