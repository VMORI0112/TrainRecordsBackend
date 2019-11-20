"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, Users, CourseTable, TrainingData, TrainData
from flask_jwt_simple import JWTManager, jwt_required, create_jwt

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

app.config['JWT_SECRET_KEY'] = 'dfsh3289349yhoelqwru9g'
jwt = JWTManager(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints

@app.route('/')
def home():
    return "<div style='text-align: center; background-color: orange'><h1>Backend running...</h1><br/><h3>Welcome back samir</h3><img src='https://media.gettyimages.com/photos/woman-sitting-by-washing-machine-picture-id117852649?s=2048x2048' width='80%' /></div>"

@app.route('/users', methods=['GET'])
def handle_users():

    if request.method == 'GET':
        users = Users.query.all()

        if not users:
            return jsonify({'msg':'User not found'}), 404

        return jsonify( [x.serialize() for x in users] ), 200

    return "Invalid Method", 404

@app.route('/coursetable', methods=['GET'])
def get_records():
    if request.method == 'GET':
        records = CourseTable.query.all()

        if not records:
            return jsonify({'msg':'Record not found'}), 404

        return jsonify( [x.serialize() for x in records] ), 200

    return "Invalid Method", 404    

@app.route('/trainingdata', methods=['GET'])
def get_records():
    if request.method == 'GET':
        records = TrainingData.query.all()

        if not records:
            return jsonify({'msg':'Record not found'}), 404

        return jsonify( [x.serialize() for x in records] ), 200

    return "Invalid Method", 404   

@app.route('/traindata', methods=['GET'])
def get_records():
    if request.method == 'GET':
        records = TrainData.query.all()

        if not records:
            return jsonify({'msg':'Record not found'}), 404

        return jsonify( [x.serialize() for x in records] ), 200

    return "Invalid Method", 404        

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
