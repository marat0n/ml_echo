import os
from flask import Flask, flash, render_template, request
from werkzeug.utils import secure_filename
import neuro


UPLOAD_FOLDER = os.path.abspath('uploaded_files')
ALLOWED_EXTENSIONS = {'mp3', 'wav'}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST', 'GET'])
def home():
    neuro_result = None

    if request.method == 'POST':
        if 'file' in request.files:
            data = request.files['file']

            if data and allowed_file(data.filename):
                filename = secure_filename(data.filename)
                data.save(os.path.join(UPLOAD_FOLDER, filename))
                pathToFile = f'{UPLOAD_FOLDER}\\{filename}'
                neuro_result = neuro.neuro(pathToFile)
            else:
                neuro_result = 'File is not allowed or no selected file'

    return render_template('home.html', neuro_result=neuro_result)


app.run(debug=True, host='185.221.153.51', port=5000)
