# importing the required libraries
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import audio2midi
from pathlib import Path

# initialising the flask app
app = Flask(__name__)

# Creating the upload folder
upload_folder = "./uploads"

# Max size of the file
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

# Configuring the upload folder
app.config['UPLOAD_FOLDER'] = upload_folder


# The path for uploading the file
@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/upload', methods=['GET', 'POST'])
def uploadfile():
    if request.method == 'POST':  # check if the method is post
        f = request.files['file']  # get the file from the files object

        # Saving the file in the required destination
        #
        file_in = os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        downloads_path = str(Path.home() / "Downloads" / "output.midi")

        f.save(file_in)  # this will secure the file

        audio2midi.run(file_in, downloads_path)
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
