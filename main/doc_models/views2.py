from main import user_namespace as ns
from flask_restplus import fields, reqparse

# post 方法 使用的 body 的接口文档参数
input_user_model = ns.model('InputUserModel', {
    'user_id': fields.Integer(required=True, description='The user unique identifier'),
    'username': fields.String(required=True, description='The user nickname'),
})

output_user_model = ns.model('OutputUserModel', {
    'id': fields.Integer(required=False, description='id'),
    'user_id': fields.Integer(required=True, description='The user unique identifier'),
    'username': fields.String(required=True, description='The user nickname'),
})

# <------------------------------------------------------------------------------------------>
# get  方法使用的 query 接口文档参数
pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('filter_all', type=int, required=False, default=0, choices=[1, 0],
                                  help='查询所有')
