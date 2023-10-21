from flask import Flask, request, render_template
from entities import Company, Employee
from base import Session
from utils import get_info, warning

app = Flask(__name__)
session = Session()

@app.route('/1', methods=['GET'])
def getComps():
    companies = list()
    for company in session.query(Company).all():
        companies.append(company.name)
    return ' '.join(companies)

@app.route('/2', methods=['GET'])
def getUsers():
    employes = list()
    for employee in session.query(Employee).all():
        employes.append(' '.join(map(str, [employee.id, employee.name, employee.surname])))
    return "\n".join(employes)
@app.route('/3', methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        position = request.form['position']
        company = request.form['company']
        company_id = session.query(Company).filter(Company.name == company).all()[0].id
        if not company_id:
            return warning()
        else:
            session.add(Employee(name, surname, position, company_id))
            session.commit()
            return 'Ok'
    else:
        return render_template('3.html')

@app.route('/4', methods=['GET', 'POST'])
def delUser():
    if request.method == 'POST':
        del_id = request.form['del_id']
        if del_id.isdigit():
            if session.query(Employee).filter(Employee.id == del_id).count():
                session.query(Employee).filter(Employee.id == del_id).delete()
                session.commit()
                return 'Ok'
            else:
                return warning()
        else:
            return warning()
    else:
        return render_template('4.html')

@app.route('/5', methods=['GET', 'POST'])
def updUser():
    if request.method == 'POST':
        upd_id = request.form['upd_id']
        if upd_id.isdigit() and session.query(Employee).filter(Employee.id == upd_id).count():#userRep.exist(upd_id):
            name = request.form['name']
            surname = request.form['surname']
            position = request.form['position']
            company = request.form['company']
            company_id = session.query(Company).filter(Company.name == company).all()[0].id#compRep.get_id(company)
            if not company_id:
                return warning()
            else:
                record_to_update = session.query(Employee).filter_by(id=upd_id).first()
                record_to_update.name = name
                record_to_update.surname = surname
                record_to_update.position = position
                record_to_update.company = company
                record_to_update.company_id = company_id
                session.commit()
                return 'ok'
    else:
        return render_template('5.html')

if __name__ == '__main__':
    app.run(port=8000)