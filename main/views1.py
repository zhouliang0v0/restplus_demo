from flask import Blueprint
from flask_restplus import Api, Namespace, Resource, fields

from main import global_namespace as ns

user_model = ns.model('UserModel', {
    'user_id': fields.String(readOnly=True, description='The user unique identifier'),
    'username': fields.String(required=True, description='The user nickname'),
})


@ns.route('/')
class ProjectResource(Resource):
    def get(self):
        return {'num': 42}

    def post(self):
        return {'num': 43}
