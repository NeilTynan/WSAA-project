from flask import Flask, request, jsonify, render_template, abort
from grantDAOskeleton import grantDAO

app = Flask(__name__)

grants = []

@app.route('/')
def home():
    return render_template('1table.html')

@app.route('/grants', methods=['GET'])
def get_grants():
    return jsonify(grantDAO.getAll())

@app.route('/grants', methods=['POST'])
def create_grant():
    jsonstring = request.json
    grant = {}
    if "title" not in jsonstring:
        abort(401)
    grant["title"] = jsonstring["title"]
    if "author" not in jsonstring:
        abort(401)
    grant["author"] = jsonstring["author"]
    if "institution" not in jsonstring:
        abort(401)
    grant["institution"] = jsonstring["institution"]
    if "amount" not in jsonstring:
        abort(401)
    grant["amount"] = jsonstring["amount"]
    return jsonify(grantDAO.create(grant))
# abort option


@app.route('/grants/<int:id>', methods=['PUT'])
def update_grant(id):
    jsonstring = request.json
    grant = {}
    if "title" in jsonstring:
        grant["title"] = jsonstring["title"]
    if "author" in jsonstring:
        grant["author"] = jsonstring["author"]
    if "institution" in jsonstring:
        grant["institution"] = jsonstring["institution"]
    if "amount" in jsonstring:
        grant["amount"] = jsonstring["amount"]
    return jsonify(grantDAO.update(id, grant))

@app.route('/grants/<int:id>', methods=['DELETE'])
def delete_grant(id):
    return jsonify(grantDAO.delete(id, grant))

if __name__ == '__main__':
    app.run(debug=True)