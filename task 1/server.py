from flask import Flask, request, render_template, jsonify, abort
from entities import Company, Employee
from base import Session
from utils import get_info, warning
import json


app = Flask(__name__)
session = Session()

@app.route('/comps', methods=['GET'])
def getComps():
    companies = list()
    for company in session.query(Company).all():
        company_dict = company.__dict__
        spec_key = company_dict.pop('_sa_instance_state')
        companies.append(company_dict)
    return json.dumps(companies)

@app.route('/users', methods=['GET'])
def getUsers():
    employes = list()
    for employee in session.query(Employee).all():
        employee_dict = employee.__dict__
        spec_key = employee_dict.pop('_sa_instance_state')
        employes.append(employee_dict)
    return json.dumps(employes)

@app.route('/users', methods=['POST'])
def addUser():
    if not request.json:
        abort(400)
    company_id = session.query(Company).filter(Company.name == request.json['company']).all()[0].id
    if not company_id:
        return warning()
    else:
        user = Employee(request.json['name'],
                        request.json['surname'],
                        request.json['position'],
                        company_id
                        )
        session.add(user)
        session.commit()
        return 'Ok'

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delUser(user_id):
    if session.query(Employee).filter(Employee.id == user_id).count():
        session.query(Employee).filter(Employee.id == user_id).delete()
        session.commit()
        return 'Ok'
    else:
        return warning()


@app.route('/users/<int:user_id>', methods=['PUT'])
def updUser(user_id):
    if not request.json:
        abort(400)
    if session.query(Employee).filter(Employee.id == user_id).count():
        company_id = session.query(Company).filter(Company.name == request.json['company']).all()[0].id
        if not company_id:
            return warning()
        else:
            record_to_update = session.query(Employee).filter_by(id=user_id).first()
            record_to_update.name = request.json['name']
            record_to_update.surname = request.json['surname']
            record_to_update.position = request.json['position']
            record_to_update.company_id = company_id
            session.commit()
            return 'ok'

if __name__ == '__main__':
    app.run(port=8000)