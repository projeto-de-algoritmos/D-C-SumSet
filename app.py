from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sum_set import sum_set_nary

app = Flask(__name__)
api = Api(app)

class SumSet(Resource):
    def post(self):
        data = request.get_json()
        req_set = data['set']
        n = data['n']
        sum_set = sum_set_nary(set(req_set), n)
        return jsonify({'sum_set': list(sum_set)})

api.add_resource(SumSet, '/sumset')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)