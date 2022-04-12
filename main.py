from  flask import Flask, render_template, request, url_for
from numpy import False_
from werkzeug.utils import secure_filename
from hashlib import md5
from os.path import join
from time import time
from PIL import Image


# start Flask App
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/media/'


@app.route('/', methods= ['GET', "POST"])
def index():
    if request.method== 'POST' :
        FileObject = request.files['file']
        mimetype = FileObject.mimetype
        if FileObject.mimetype == "image/jpeg":
            filename =join(app.config["UPLOAD_FOLDER"],
             secure_filename(md5(str(time()).encode()).hexdigest()+'.png'))
            FileObject = Image.open(FileObject)
            FileObject.save(filename)
            return render_template('index.html', filename=filename)
        else:
            return render_template('index.html', mimetype=mimetype)  # For extra security

    return render_template('index.html')

if __name__ == '__main__':
    
    app.run(debug= True)
