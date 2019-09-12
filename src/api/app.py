"""This module has the App and Routes of API

"""

from flask import Flask
from flask_restful import Resource, Api

APP = Flask(__name__)
API = Api(APP)


class DevOps(Resource):
    """The DevOps Resource

    """
    def get(self):
        """The get method of this resource

        :return: Return welcome to the candidate
        :rtype: dict
        """
        return {
            'candidate': 'Welcome to the DevOps test'
        }


API.add_resource(DevOps, '/')

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0')
