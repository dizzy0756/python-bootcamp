from flask import request
from model.student import Student
from database import database
import sqlite3

def generate_routes(app):

    def validate_request_body(data):

        if data is None:
            return {
                "message" : "Request body should contain valid json file"
            }, 400
        
        required_fields = ["id","name","course","age"]
        for field in required_fields:
            if field not in data:
                return {
                    "message" : f"Missing required field {field}"
                }, 400

        if not isinstance(data["id"],int):
            return {
                "message" : "Id must be an integer value"
            }, 400
        if not isinstance(data["age"],int):
            return {
                "message" : "Age must be an integer value"
            }, 400
        if not isinstance(data["name"],str):
            return {
                "message" : "Name must be a string"
            }, 400
        if not isinstance(data["course"],str):
            return {
                "message" : "Course must be a string"
            }, 400
            
        if not data["name"].strip():
            return {
                "message" : "Name cannot be empty"
            }, 400
        if not data["course"].strip():
            return {
                "message" : "Course cannot be empty"
            }, 400
        
        if data["id"] <= 0:
            return {
                "message" : "Id must be a positive integer"
            }, 400    
        if data["age"] < 18:
            return {
                "message" : "Student must be 18 or above"
            }, 400
        
        return None      

    @app.post("/students")
    def add_student():
        data = request.get_json()

        error = validate_request_body(data)
        if error:
            return error
        
        student = Student.from_dict(data)

        try:
            database.add(student)
        except sqlite3.IntegrityError:
            return {
                "message" : "Student ID already exist"
            }, 409
        
        return {
            "message" : "Students added successfully"
        }, 201
    
    @app.put("/students/<int:id>")
    def update_student(id):
        data = request.get_json()
        error = validate_request_body(data)
        if error:
            return error
        student = Student.from_dict(data)
        if id == student.id:
            result = database.update(student)
            if result == 0:
                return{
                    "message" : "Student not found"
                }, 404
            else:
                return{
                    "message" : "Student updated successfully"
                }, 200
        else:
            return {
                "message" : "Student id address do not match with the id in the request body"
            }, 400
    
    @app.delete("/students/<int:id>")
    def delete_student(id):
        result = database.delete(id)
        if result == 0:
            return {
                "message" : "Student not found"
            }, 404
        else:
            return {
                "message" : "Student deleted successfully"
            }, 200
        
    @app.get("/students/<int:id>")
    def search_student(id):
        result = database.search(id)
        if result is None:
            return {
                "message" : "Student not found"
            }, 404
        else:
            return result, 200
        
    @app.get("/students")
    def view_students():
        students = database.view()
        return [student.to_dict() for student in students]