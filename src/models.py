from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120) )
    password = db.Column(db.String(80), nullable=False)
    avatar = db.Column(db.String(220), default='avatar.png')
    

    def __repr__(self):
        return '<Users %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "avatar": self.avatar,
        }
class CourseTable(db.Model):
    courseNumber = db.Column(db.Integer)
    category = db.Column(db.String(30)) 
    descriptionName = db.Column(db.String(60)
    dataType = db.Column(db.String(10))
    recurrent = db.Column(db.String(1))
    hours = db.Column(db.String(3))
    days = db.Column(db.Decimal(7, 2))
    hours = db.Column(db.String(3))
    companyTrainer = db.Column(db.String(6))
    sta = db.Column(db.String(1))
   
    def serialize(self):
        return {
            "CourseNumber": self.courseNumber,
            "Category": self.category,
            "DescriptionName": self.descriptionName,
            "DataType": self.dataType,
            "CourseRecurrence": self.recurrent,
            "HoursCourse ": self.hours,
            "DaysCourse": self.days,
            "CompanyTrainer": self.companyTrainer,
            "Status": self.sta,
        }
class TrainingData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseNumber = db.Column(db.Integer)
    hasRecu = db.Column(db.String(1)) 
    dateAtten = db.Column(db.Datetime)
    ceCo = db.Column(db.String(12))
    trainingGroup = db.Column(db.String(30))
    name = db.Column(db.String(40))
    sta = db.Column(db.String(1))
    a&P = db.Column(db.Integer)
    
    def serialize(self):
        return {
            "id": self.id,
            "CourseNumber": self.courseNumber,
            "HasRecurrent": self.hasRecu,
            "DateAtten": self.dateAtten,
            "CostCenter": self.ceCo,
            "TrainingGroup": self.trainingGroup,
            "Name": self.name,
            "Status": self.sta,
            "A&PLicense": self.a&P,
            "InstrutorInitials": self.insIni,
        }
class TrainData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseNumber = db.Column(db.Integer)
    hasRecu = db.Column(db.String(1)) 
    descriptionName = db.Column(db.String(60)
    dateAtten = db.Column(db.Datetime)
    ceCo = db.Column(db.String(12))
    trainingGroup = db.Column(db.String(30))
    name = db.Column(db.String(40))
    hours = db.Column(db.String(3))
    days = db.Column(db.Decimal(7, 2))
    sta = db.Column(db.String(1))
    a&P = db.Column(db.Integer)
    insIni = db.Column(db.String(3))
    recurrent = db.Column(db.String(1)) 
    oneYearExpire = db.Column(db.Datetime)
    twoYearExpire = db.Column(db.Datetime)
    threeYearExpire = db.Column(db.Datetime)
    fourYearExpire = db.Column(db.Datetime)

    def serialize(self):
        return {
            "id": self.id,
            "CourseNumber": self.courseNumber,
            "HasRecurrent": self.hasRecu,
            "DescriptionName": self.descriptionName,
            "DateAtten": self.dateAtten,
            "CostCenter": self.ceCo,
            "TrainingGroup": self.trainingGroup,
            "Name": self.name,
            "Status": self.sta,
            "A&PLicense": self.a&P,
            "InstrutorInitials": self.insIni,
            "CourseRecurrence": self.recurrent,
            "TwoYearExpire": self.TwoYearExpire,
            "ThreeYearExpire": self.ThreeYearExpire,
        }




