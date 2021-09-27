from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sum_set import sum_set_nary, sum_set 

app = Flask(__name__)
api = Api(app)

class SumSet(Resource):
    def post(self):
        data = request.get_json()
        set_A = data['A']
        set_B = data['B']
        sum = sum_set(set(set_A), set(set_B))
        return jsonify({'sum_set': list(sum)})

class Multiply(Resource):
    def post(self):
        data = request.get_json()
        req_set = data['set']
        n = data['n']
        sum_set = sum_set_nary(set(req_set), n)
        return jsonify({'multiply': list(sum_set)})

api.add_resource(SumSet, '/sumset')
api.add_resource(Multiply, '/multiply')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)