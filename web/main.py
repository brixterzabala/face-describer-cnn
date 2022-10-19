import sqlite3
from flask import Flask, redirect, url_for,session,jsonify, render_template, request, make_response
from eyes import *
from nose import *
from skin import *
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)


app = Flask(__name__)
app.secret_key = "sk1rt"



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    base64String = str.encode(request.json['base64Image'][23:])

    with open("uploads/img.jpg", "wb") as fh:
        fh.write(base64.decodebytes(base64String))

    eyes = classifyEyes('uploads/img.jpg')
    nose = classifyNose('uploads/img.jpg')
    skin = classifySkin('uploads/img.jpg')

    return jsonify({
        "eyes": eyes,
        "nose": nose,
        "skin": skin,
    }), 200




@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/developer")
def developer():
    return render_template('developer.html')
    

if __name__ == '__main__':
    app.run(debug=True)
