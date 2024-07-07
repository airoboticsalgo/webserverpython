# blueprint_module\__init__.py

from flask import Blueprint

blueprint = Blueprint('my_blueprint', __name__)

from . import app3,app2
# from . import app3