"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap, sha256
from models import db, Users, CourseTable, TrainingData, TrainData, datarecord
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
    return "<div style='text-align: center; background-color: orange'><h1>Backend running...</h1><br/><h3>Welcome</h3><img src='https://media.gettyimages.com/photos/woman-sitting-by-washing-machine-picture-id117852649?s=2048x2048' width='80%' /></div>"

@app.route('/users', methods=['GET'])
def handle_users():

    if request.method == 'GET':
        users = Users.query.all()

        if not users:
            return jsonify({'msg':'User not found'}), 404

        return jsonify( [x.serialize() for x in users] ), 200

    return "Invalid Method", 404

@app.route('/getrecords', methods=['GET'])
def handle_records():

    if request.method == 'GET':
        records = datarecord.query.all()

        if not records:
            return jsonify({'msg':'User not found'}), 404

        return jsonify( [x.serialize() for x in records] ), 200

    return "Invalid Method", 404

@app.route('/login', methods=['POST'])
def handle_login():

    body = request.get_json()

    user = Users.query.filter_by(email=body['email'], password=sha256(body['password'])).first()

    if not user:
        return 'User not found', 404

    return jsonify({
              'token': create_jwt(identity=1),
              'id': user.id,
              'email': user.email,
              'firstname': user.firstname,
              'lastname': user.lastname,
              'avatar': user.avatar
            
              })

@app.route('/register', methods=['POST'])
def handle_register():

    body = request.get_json()

    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'firstname' not in body and 'lastname' not in body:
        raise APIException("You need to specify the first name and last name", status_code=400)
    if 'password' not in body and 'email' not in body:
        raise APIException("You need to specify the password and email", status_code=400)
    if 'firstname' not in body:
        raise APIException('You need to specify the first name', status_code=400)
    if 'lastname' not in body:
        raise APIException('You need to specify the last name', status_code=400)
    if 'password' not in body:
        raise APIException('You need to specify the password', status_code=400)
    if 'email' not in body:
        raise APIException('You need to specify the email', status_code=400)



    db.session.add(Users(
        email = body['email'],
        firstname = body['firstname'],
        lastname = body['lastname'],
        password = sha256(body['password'])
    ))
    db.session.commit()

    return jsonify({
        'register': 'success',
        'msg': 'Successfully Registered'
    })

@app.route('/coursetable', methods=['GET'])
def get_coursetable():
    if request.method == 'GET':
        records = CourseTable.query.all()

        if not records:
            return jsonify({'msg':'Record not found'}), 404

        return jsonify( [x.serialize() for x in records] ), 200

    return "Invalid Method", 404    

@app.route('/trainingdata', methods=['GET'])
def get_trainingdata():
    if request.method == 'GET':
        records = datarecord.query.all()
        if not records:
            return jsonify({'msg':'Record not found'}), 404
        return jsonify( [x.serialize() for x in records] ), 200
    return "Invalid Method", 404   

@app.route('/traindata', methods=['POST'])
def get_traindata():
    if request.method == 'POST':

        body = request.get_json()
        records = datarecord.query.filter_by(employerId=body['employerId']).order_by(datarecord.dateAtten.desc())

        if not records:
            return jsonify({'msg':'Record not found'}), 404

        return jsonify( [x.serialize() for x in records] ), 200

    return "Invalid Method", 404 
@app.route('/traindata_update', methods=['POST'])
def get_traindata_update():
    if request.method == 'POST':

        body = request.get_json()
        records = datarecord.query.filter_by(employerId=body['employerId'], courseNumber=body['courseNumber']).first()

        if not records:
            return jsonify({'msg':'Record not found'}), 404

        # return jsonify( [x.serialize() for x in records] ), 200
        return jsonify(records.serialize()), 200

    return "Invalid Method", 404 
@app.route('/gettraindata', methods=['GET'])
def get_traindat():
    if request.method == 'GET':
        records = datarecord.query.all()
        if not records:
            return jsonify({'msg':'Record not found'}), 404
        return jsonify( [x.serialize() for x in records] ), 200
    return "Invalid Method", 404   

@app.route('/deltraindata/<int:employ_id>/<int:course_number>', methods=['DELETE'])
def del_traindata(employ_id, course_number):
        course = datarecord.query.filter_by(employerId=employ_id, courseNumber=course_number).first()
        db.session.delete(course)
        db.session.commit()
        return "ok", 200


@app.route('/updatetraindata/<int:employ_id>/<int:course_number>', methods=['PUT'])
def update_data(employ_id, course_number):
     
        body = request.get_json()
        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        course = datarecord.query.filter_by(employerId=employ_id, courseNumber=course_number).first()
        if course is None:
            raise APIException('User not found', status_code=404)
        print('$#$', course.courseNumber)
        if "employerId" in body:
            course.employerId = body["employerId"]
        if "courseNumber" in body:
            course.courseNumber = body["courseNumber"]
        if "hasRecu" in body:
            course.hasRecu = body["hasRecu"]
        if "descriptionName" in body:
            course.descriptionName = body["descriptionName"]
        if "dateAtten" in body:
            course.dateAtten = body["dateAtten"]
        if "ceCo" in body:
            course.ceCo = body["ceCo"]
        if "trainingGroup" in body:
            course.trainingGroup = body["trainingGroup"]    
        if "name" in body:
            course.name = body["name"]
        if "hours" in body:
            course.hours = body["hours"]
        if "days" in body:
            course.days = body["days"]
        if "sta" in body:
            course.sta = body["sta"]
        if "anp" in body:
            course.anp = body["anp"]
        if "insIni" in body:
            course.insIni = body["insIni"]
        if "recurrent" in body:
            course.recurrent = body["recurrent"]   
        if "oneYearExpire" in body:
            course.oneYearExpire = body["oneYearExpire"]
        if "twoYearExpire" in body:
            course.twoYearExpire = body["twoYearExpire"]
        if "threeYearExpire" in body:
            course.threeYearExpire = body["threeYearExpire"]
        if "fourYearExpire" in body:
            course.fourYearExpire = body["fourYearExpire"]  

        db.session.commit()
        return jsonify(course.serialize()), 200
   

@app.route('/addrecord', methods=['POST'])
def add_traindata():

    body = request.get_json()

    db.session.add(datarecord(
        employerId = body['employerId'],
        courseNumber = body['courseNumber'],
        hasRecu = body['hasRecu'],
        descriptionName = body['descriptionName'],
        dateAtten = body['dateAtten'],
        ceCo = body['ceCo'],
        trainingGroup = body['trainingGroup'],
        name = body['name'],
        hours = body['hours'],
        days = body['days'],
        sta = body['sta'],
        anp = body['anp'],
        insIni = body['insIni'],
        recurrent = body['recurrent'],
        oneYearExpire = body['oneYearExpire'],
        twoYearExpire = body['twoYearExpire'],
        threeYearExpire = body['threeYearExpire'],
        fourYearExpire = body['fourYearExpire']
   
    ))
    db.session.commit()

    return jsonify({
        'Added': 'success',
        'msg': 'Successfully Record added'
    })    


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
