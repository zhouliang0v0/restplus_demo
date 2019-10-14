from flask_restplus import Resource, fields, reqparse

from common import ArgsMixIn
from main import user_namespace as ns
from main.args.views2 import args_get, args_put_or_post
from main.doc_models.views2 import input_user_model, output_user_model, pagination_arguments


@ns.route('/')
class UserManage(ArgsMixIn, Resource):

    # @ns.expect(GetModel)
    @ns.expect(pagination_arguments, validate=True)
    def get(self):
        args = self._get_args(args_get)
        print(args['filter_all'])
        return {'num': 42}

    def post(self):
        return {'num': 43}


@ns.route('/<int:id>')
@ns.param('id', 'The user identifier')
class UserEditManage(ArgsMixIn, Resource):

    # @ns.doc('update project')
    @ns.expect(input_user_model)
    @ns.marshal_with(output_user_model)
    def put(self, id):
        args = self._get_args(args_put_or_post)

        return {'id': id, 'username': args['username'], 'user_id': args['user_id']}

    @ns.expect(input_user_model)
    @ns.marshal_with(output_user_model)
    def delete(self, id):
        return {'id': id}
