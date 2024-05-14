from flask import Blueprint, request, jsonify
from employee.database import add, delete, update, view

employee_bp = Blueprint('employee', __name__, url_prefix='/employee')

@employee_bp.route("/",methods=['POST'])
def add_employee():
    if request.form.get('name') and request.form.get('position') and request.form.get('salary'):
        data = request.form
        return add(data),201
    else:
        return jsonify({'error':'Bad Request','message':'Pls send name, position and salary to add data.'}),400

@employee_bp.route("/",methods=['DELETE'])
def delete_employee():
    if request.form.get('employee_id') and request.form.get('name') and request.form.get('position') and request.form.get('salary'):
        data = request.form
        return delete(data),200
    else:
        return jsonify({'error':'Bad Request','message':'Pls send employee_id, name, position and salary to delete data.'}),400

@employee_bp.route("/",methods=['PUT'])
def update_employee():
    if request.form.get('employee_id') and request.form.get('name') and request.form.get('position') and request.form.get('salary'):
        data = request.form
        return update(data),200
    else:
        return jsonify({'error':'Bad Request','message':'Pls send employee_id, name, position and salary to update data.'}),400

@employee_bp.route("/",methods=['GET'])
def view_db():
    data = request.args
    return view(data),200