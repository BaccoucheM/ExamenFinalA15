from flask import Flask, request, jsonify
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    if 'Code_projet' not in data or 'Description' not in data:
        return jsonify({'error': 'Champs Code_projet et Description obligatoires'}), 400
    project = db.create_project(data['Code_projet'], data['Description'])
    return jsonify(project), 201

@app.route('/projects/<project_code>', methods=['GET'])
def get_project(project_code):
    project = db.get_project(project_code)
    if project is None:
        return jsonify({'error': 'Projet non trouvé'}), 404
    return jsonify(project), 200

if __name__ == '__main__':
    app.run(debug=True)
