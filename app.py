from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)
#########################################
###               DB키제거             ###
#########################################
application = Flask(import_name=__name__)
db = client.makeCool


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/main')
def main():
    return render_template('main.html')


@app.route("/api/main/neck", methods=["GET"])
def necklist_get():
    list_neck = list(db.neck.find({}, {'_id': False}))
    return jsonify({'main_list': list_neck})


@app.route("/api/main/waist", methods=["GET"])
def waistlist_get():
    list_waist = list(db.waist.find({}, {'_id': False}))
    return jsonify({'main_list': list_waist})


@app.route("/api/main/wrist", methods=["GET"])
def wristlist_get():
    list_wrist = list(db.wrist.find({}, {'_id': False}))
    return jsonify({'main_list': list_wrist})


@app.route("/api/main/lowerBody", methods=["GET"])
def lowerBodylist_get():
    list_lowerBody = list(db.lowerBody.find({}, {'_id': False}))
    return jsonify({'main_list': list_lowerBody})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
