from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
kpas = []
next_id = 1

# Add a KPA
@app.route('/kpa', methods=['POST'])
def add_kpa():
    global next_id
    data = request.get_json()
    new_kpa = {
        'id': next_id,
        'name': data.get('name'),
        'description': data.get('description')
    }
    kpas.append(new_kpa)
    next_id += 1
    return jsonify(new_kpa), 201

# Get all KPAs
@app.route('/kpa', methods=['GET'])
def get_all_kpas():
    return jsonify(kpas)

# Get KPA by ID
@app.route('/kpa/<int:kpa_id>', methods=['GET'])
def get_kpa(kpa_id):
    for kpa in kpas:
        if kpa['id'] == kpa_id:
            return jsonify(kpa)
    return jsonify({'error': 'KPA not found'}), 404

# Update a KPA
@app.route('/kpa/<int:kpa_id>', methods=['PUT'])
def update_kpa(kpa_id):
    data = request.get_json()
    for kpa in kpas:
        if kpa['id'] == kpa_id:
            kpa['name'] = data.get('name', kpa['name'])
            kpa['description'] = data.get('description', kpa['description'])
            return jsonify(kpa)
    return jsonify({'error': 'KPA not found'}), 404

# Delete a KPA
@app.route('/kpa/<int:kpa_id>', methods=['DELETE'])
def delete_kpa(kpa_id):
    for kpa in kpas:
        if kpa['id'] == kpa_id:
            kpas.remove(kpa)
            return jsonify({'message': 'KPA deleted'})
    return jsonify({'error': 'KPA not found'}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
