from flask import Flask, request, jsonify, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename
from numpy import loadtxt
import os


app = Flask(__name__)

UPLOAD_FOLDER = "Solucion_semana2/uploads"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
#Define the path to the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#Specifies the maximum size (in bytes) of the files to be uploaded  
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'
            
        file = request.files['file']

        if file.filename == '':
            return 'No selected file'
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for("get_file", filename=filename))
        else:
            return 'No allowed extension'

@app.route("/uploads/<filename>")
def get_file(filename): 
    #filename = send_from_directory(app.config["UPLOAD_FOLDER"], filename)
    #raw_data = open(filename, 'r')
    #data = loadtxt(raw_data, delimiter=",")
    #print(data.shape)
    
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)



if __name__ == '__main__':
    app.run(debug=True)