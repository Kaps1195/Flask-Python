from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

import json as js

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Kapil/Desktop/Kapil_Assignment/Kapil_Assignment/organization.db' # dialect+driver://username:password@host:port/database

db = SQLAlchemy(app)

class Employees(db.Model):
    __tablename__ = 'employees'

    id = db.Column('Employee_ID',db.Integer,primary_key=True)
    first_name = db.Column('First_name',db.String)
    last_name = db.Column('Last_name',db.String)
    device_id = db.Column('Device_ID',db.Integer)

    def getById(self,id):
        emp = Employees.query.filter_by(id=id).first()
        val = {"id":emp.id, "first_name":emp.first_name,"last_name":emp.last_name,"device_id":emp.device_id}
        return js.dumps(val)

    def getAll(self):
        emp_all =  Employees.query.all()
        vals = []
        for emp in emp_all:
            val = {"id":emp.id, "first_name":emp.first_name,"last_name":emp.last_name,"device_id":emp.device_id}
            vals.append(val)
        print(vals)
        return js.dumps(vals)


    def insert(self,kwargs):
        db.session.add(Employees(**kwargs))
        db.session.commit()
    
    def update(self,id,kwargs):
        Employees.query.filter_by(id=id).update(kwargs)
        db.session.commit()
    
    def delete(self,id):
        self = Employees.query.filter_by(id=id).first()
        print(self)
        db.session.delete(self)
        db.session.commit()


@app.route('/',methods=['GET'])
def getAll():
    text = Employees().getAll()
    # emp = Employees()
    return text

@app.route('/<int:id>', methods=['GET'])
def getByID(id):
    text = Employees().getById(id)
    return text

@app.route('/',methods=['POST'])
def insert():
    data = {}
    data["id"] = request.form["id"]
    data["first_name"] = request.form["first_name"]
    data["last_name"] = request.form["last_name"]
    data["device_id"] = request.form["device_id"]
    #pprint.pprint(data)
    Employees().insert(data)
    return "Inserted"

@app.route('/<int:id>',methods=['GET','PATCH'])
def update(id):
    data = {}
    data["id"] = request.form["id"]
    data["first_name"] = request.form["first_name"]
    data["last_name"] = request.form["last_name"]
    data["device_id"] = request.form["device_id"]
    Employees().update(id,data)
    return "UPDATED"

@app.route('/<int:id>',methods=['DELETE'])
def delete(id):
    Employees().delete(id)
    return "DELETED!"