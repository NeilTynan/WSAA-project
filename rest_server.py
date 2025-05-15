from flask import Flask, request, jsonify, render_template, abort
from grantDAO import researcherDAO

app = Flask(__name__)

grants = []

# HTML

@app.route('/')
def home():
    return render_template('1table.html')


# Researcher Table CRUD

@app.route('/researcher/<int:id>', methods=['GET'])
def find_by_idresearcher(id):
    return jsonify(researcherDAO.findByIDResearcher(id))

@app.route('/researcher', methods=['GET'])
def get_researcher():
    return jsonify(researcherDAO.getAllResearcher())

@app.route('/researcher', methods=['POST'])
def create_researcher():
    jsonstring = request.json
    researcher = {}
    if "title" not in jsonstring:
        abort(400)
    researcher["title"] = jsonstring["title"]
    if "author" not in jsonstring:
        abort(400)
    researcher["author"] = jsonstring["author"]
    if "year" not in jsonstring:
        abort(400)
    researcher["year"] = jsonstring["year"]
    if "institution" not in jsonstring:
        abort(400)
    researcher["institution"] = jsonstring["institution"]
    if "programme" not in jsonstring:
        abort(400)
    researcher["programme"] = jsonstring["programme"]
    if "amount" not in jsonstring:
        abort(400)
    researcher["amount"] = jsonstring["amount"]
    return jsonify(researcherDAO.createResearcher(researcher))

@app.route('/researcher/<int:id>', methods=['PUT'])
def update_researcher(id):
    jsonstring = request.json
    researcher = {}
    if "title" in jsonstring:
        researcher["title"] = jsonstring["title"]
    if "author" in jsonstring:
        researcher["author"] = jsonstring["author"]
    if "year" in jsonstring:
        researcher["year"] = jsonstring["year"]
    if "institution" in jsonstring:
        researcher["institution"] = jsonstring["institution"]
    if "programme" in jsonstring:
        researcher["programme"] = jsonstring["programme"]
    if "amount" in jsonstring:
        researcher["amount"] = jsonstring["amount"]
    return jsonify(researcherDAO.updateResearcher(id, researcher))

@app.route('/researcher/<int:id>', methods=['DELETE'])
def delete_researcher(id):
    return jsonify(researcherDAO.deleteResearcher(id))

# Comparison functions

@app.route('/compare/<int:id>')
def compare(id):
    result = researcherDAO.compareResearcherAmount(id)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)