from flask import Flask, jsonify, request
from ssh import ssh_conn

app = Flask(__name__)
incomes = [
    {'description': 'salary', 'amount': 5000}
]

@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204

@app.route("/")
def hello_world():
    # sys.exit()
    return ssh_conn()
