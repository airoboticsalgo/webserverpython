from flask import Flask,flash, request, redirect, url_for
from flask import request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "dataset"
ALLOWED_EXTENSIONS = {'jpg'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET'])
def hello_world():
    print("test")
    return  "test1"

@app.route("/filecreate", methods=['POST'])
def filecreate():
    user = request.args.get('test')
    print("test")
    return  user

@app.route("/fileupload", methods=['PUT'])
def fileupload():
     user = request.args.get('test')
     if 'file' not in request.files:
         
         print("request.files",request.files)
         flash('No file multipart ')
         return redirect(request.url)
     file = request.files['file']
     if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
     
     if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
     return  user