from flask import Blueprint
from flask_restplus import Api, Namespace

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)
global_namespace = Namespace('global', path='/api/v1.0/global')
user_namespace = Namespace('user', path='/api/v1.0/user')

from main import views1
from main import views2

api.add_namespace(global_namespace)
api.add_namespace(user_namespace)
