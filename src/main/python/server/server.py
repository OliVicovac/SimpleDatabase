from flask import Flask;
from flask_restful import Resource, Api, reqparse
import sqlite3

app = Flask(__name__)
api = Api(app)

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')

    def execute(self, query):
        rs = []
        for row in self.conn.execute(query):
            rs.append(row)
        self.conn.commit()
        return rs

    def close(self):
        self.conn.close()

class Student(Resource):

    def __init__(self):
        self.db = Database()
        self.db.execute('''CREATE TABLE IF NOT EXISTS student
                        (email text, name text, picture text)''')

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str)
        parser.add_argument('name', type=str)
        parser.add_argument('picture', type=str)
        self.db.execute("INSERT INTO student VALUES ("+parser.parse_args().email+","+parser.parse_args().name+","+parser.parse_args().picture+")")
        return "success!"

    def get(self):
        return self.db.execute("SELECT * FROM student")

api.add_resource(Student, "/students")

if __name__=="__main__":
    app.run(debug=True)