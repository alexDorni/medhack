import os

# from apispec import APISpec
# from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
# from flask_apispec.extension import FlaskApiSpec
from .config import config

basedir = os.path.abspath(os.path.dirname(__file__))
server = Flask(__name__)
api = Api(server)

# server.config.update({
#     'APISPEC_SPEC': APISpec(
#         title='Flask CV',
#         version='v1',
#         plugins=[MarshmallowPlugin()],
#         openapi_version='2.0.0'
#     ),
#     'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
#     'APISPEC_SWAGGER_UI_URL': '/'  # URI to access UI of API Doc
# })
# docs = FlaskApiSpec(server)

environment = os.getenv('FLASK_ENV', 'development')

print(f"using environment: {environment}")

server.config.from_object(config[environment])

db = SQLAlchemy(server)
ma = Marshmallow(server)
migrate = Migrate(server, db)
