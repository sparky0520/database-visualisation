from flask import Flask,request,jsonify,Blueprint
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS and handle preflight requests
CORS(app, resources={r"/*": {"origins": "*"}})

from employee.routes import employee_bp
app.register_blueprint(employee_bp)

if __name__ == '__main__':
    app.run(debug=True)