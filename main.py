import os
import boto3
from flask import Flask, flash, render_template, redirect, request, url_for
from werkzeug.utils import secure_filename
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.secret_key = '23ab4e7c9fd44e1c92cd7f91a78ef650'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name='us-east-1'
)


BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

@app.route('/')

def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No file has been selected')
        return redirect(request.url)
    
    if file:
        secure_input = secure_filename(file.filename)
        try:
            s3.upload_fileobj(file, BUCKET_NAME, secure_input)
            flash('The file has been uploaded')
        except Exception as e:
            flash(f'File upload failed:" {e}')
        return redirect(url_for('index')) 

if __name__ == '__main__':
    app.run(debug=True)


    
        

