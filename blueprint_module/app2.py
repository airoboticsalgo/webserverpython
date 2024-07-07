from . import blueprint

import os
# app = Flask(__name__)
# app = Blueprint('simple_page', __name__, template_folder='templates')
# from __main__ import app

@blueprint.route("/fileread", methods=['GET'])
def fileread():
    print("test")
    return  "test2"