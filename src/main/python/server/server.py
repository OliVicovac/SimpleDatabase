from flask import Flask;
from flask_restful import Resource, Api, reqparse
import sqlite3

app = Flask(__name__)
api = Api(app)

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')

    def execute(self, query):
        returnVal = self.conn.execute(query)
        self.conn.commit()
        return returnVal

    def close(self):
        self.conn.close()

class Student(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str)
    parser.add_argument('name', type=str)
    parser.add_argument('picture', type=str)

    def __init__(self):
        self.db = Database()

    def post(self):
        self.db.execute('''CREATE TABLE student
                        (email text, name text, picture text)''')
        return "Formular"

api.add_resource(Student, "/students")

if __name__=="__main__":
    app.run(debug=True)