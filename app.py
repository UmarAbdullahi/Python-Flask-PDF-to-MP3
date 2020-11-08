# Importing the necessary Libraries
import os
import os.path
from flask_cors import cross_origin
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from main import text_to_speech

app = Flask(__name__)
#os.path.abspath()

@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def homepage():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
            cwd = os.path.abspath(uploaded_file.filename)
            
            text = cwd
            gender = request.form['voices']
            text_to_speech(text, gender)
        return redirect(url_for('homepage'))
    else:
        return render_template('frontend.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True)

