from flask import Flask, abort, jsonify, request
from flask_cors import CORS
import ga_mip as ga
import exemplo_mapa as mapa

app = Flask(__name__)
CORS(app) 

items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    return jsonify(item) if item else ('', 404)

@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/ga', methods=['POST'])
def calcular():
    data = request.json

    if not data or not all(k in data for k in ('profit', 'weight', 'capacity')):
        abort(400, description='Dados insuficientes: é necessário fornecer profit, weight e capacity.')

    profit = data['profit']
    weight = data['weight']
    capacity = data['capacity']

    if not isinstance(profit, list) or not isinstance(weight, list) or not isinstance(capacity, (int, float)):
        abort(400, description='Os dados devem estar nos formatos corretos.')

    resultado = ga.calcularLucro(profit, weight, capacity)

    print(resultado)
    return jsonify({'resultado': resultado}), 200

@app.route('ga/mapa', method=['POST'])
def calcularMapa():
    data = request.json

    places = data['places']
    dists = data['dists']

    resultado = mapa.executar(places, dists)
    return jsonify({'resultado': resultado}), 200


if __name__ == '__main__':
    app.run(debug=True)