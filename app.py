from flask import Flask,flash, request, redirect, url_for
from flask import request
from werkzeug.utils import secure_filename
from blueprint_module import blueprint
import os
# import app2
app = Flask(__name__)
app.register_blueprint(blueprint)
def createdir(path):
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, path)
    if not os.path.exists(final_directory):
     os.makedirs(final_directory)
    return

# app.ad
dataset="dataset"
createdir(dataset)
app.config['UPLOAD_FOLDER'] = dataset
ALLOWED_EXTENSIONS = {'jpg'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route("/filecreate", methods=['POST'])
def filecreate():
    user = request.args.get('test')
    print("test=",user)
    return  str(user)

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
     return  str(user)

if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()