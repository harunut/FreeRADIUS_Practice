from utils import sendAuthRequest
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json
import requests

MAIN_API_URL:str = "http://localhost:5000/API/mainAPI"
SUB_API_URL:str = "http://localhost:5000/API/subAPI"

app = Flask(__name__)
api = Api(app)

class MainResource(Resource):
    def post(self):
        ID:str = str(request.form['ID'])
        PW:str = str(request.form['PW'])
        AUTH:str = str(request.form['AUTH'])
        data = json.dumps(sendAuthRequest(id=ID, pw=PW, auth=AUTH))
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(url=SUB_API_URL, data=data, headers=headers)
        return response.json()


class SubResource(Resource):
    def post(self):
        req_data:json = request.get_json()
        userName:str = req_data["userName"]
        password:str = req_data["password"]
        auth:str = req_data["auth"]
        result:str = req_data["result"]
        if result == "Access-Accept":
            return "Authentication Success", 200
        elif result == "Failed, Access-Reject":
            return "Authentication Faild", 401
        else:
            return "Invalid Result Value", 400

# Resource클래스를 이용하여 각 API 앤드포인트 지정
api.add_resource(MainResource,'/API/mainAPI')
api.add_resource(SubResource, '/API/subAPI')


if __name__ == '__main__':
    app.run(port = 5000, debug=True)