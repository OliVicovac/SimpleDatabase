from flask import Flask;
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def post(self):
        return "Formular"

api.add_resource(Student, "/students")

if __name__=="__main__":
    app.run(debug=True)