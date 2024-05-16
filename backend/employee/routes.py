from flask import Blueprint, request, jsonify
from employee.database import add, delete, update, view

employee_bp = Blueprint('employee', __name__, url_prefix='/employee')


@employee_bp.route("/<name>", methods=['POST'])
def add_employee(name):
    data = request.get_json()
    if name and data['position'] and data['salary']:
        return add(name,data), 201
    else:
        return jsonify({'error': 'Bad Request', 'message': 'Pls send name, position and salary to add data.'}), 400


@employee_bp.route("/<int:employee_id>", methods=['DELETE'])
def delete_employee(employee_id):
    if employee_id:
        return delete(employee_id), 200
    else:
        return jsonify(
            {'error': 'Bad Request', 'message': 'Pls send employee_id, name, position and salary to delete data.'}), 400


@employee_bp.route("/<int:employee_id>", methods=['PUT'])
def update_employee(employee_id):
    if employee_id and request.json.get('name') and request.json.get(
            'position') and request.json.get('salary'):
        data = request.json
        return update(employee_id,data), 200
    else:
        return jsonify(
            {'error': 'Bad Request', 'message': 'Pls send employee_id, name, position and salary to update data.'}), 400


@employee_bp.route("/", methods=['GET'])
def view_db():
    data = request.args
    return view(data), 200
