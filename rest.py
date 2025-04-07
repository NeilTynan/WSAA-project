from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Research Ireland Grants API!"

grants = []

@app.route('/grants', methods=['GET'])
def get():
    return jsonify(grants)

@app.route('/grants', methods=['POST'])
def create():
    new_grant = request.json
    grants.append(new_grant)
    return jsonify(new_grant), 201

@app.route('/grants/<int:grant_id>', methods=['PUT'])
def update(grant_id):
    updated_grant = request.json
    grants[grant_id] = updated_grant
    return jsonify(updated_grant)

@app.route('/grants/<int:grant_id>', methods=['DELETE'])
def delete_grant(grant_id):
    deleted_grant = grants.pop(grant_id)
    return jsonify(deleted_grant)

if __name__ == "__main__":
    app.run(debug=True)