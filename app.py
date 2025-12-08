from datetime import datetime
import os
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

# Config through environment variables
DB_USER = os.environ.get("MYSQL_USER", "root")
DB_PASSWORD = os.environ.get("MYSQL_PASSWORD", "password")
DB_HOST = os.environ.get("MYSQL_HOST", "db")
DB_PORT = os.environ.get("MYSQL_PORT", "3306")
DB_NAME = os.environ.get("MYSQL_DATABASE", "students_db")

DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    city = db.Column(db.String(120), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "city": self.city,
            "created_at": self.created_at.isoformat(),
        }

@app.before_first_request
def create_tables():
    # Create tables if they don't exist
    db.create_all()

@app.route("/")
def index():
    return "Student API is running"

# Create Student
@app.route("/student", methods=["POST"])
def create_student():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "name is required"}), 400

    student = Student(
        name=data.get("name"),
        age=data.get("age"),
        city=data.get("city"),
    )
    db.session.add(student)
    db.session.commit()
    return jsonify(student.to_dict()), 201

# Get All Students
@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.order_by(Student.created_at.desc()).all()
    return jsonify([s.to_dict() for s in students]), 200

# Get Single Student
@app.route("/student/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "student not found"}), 404
    return jsonify(student.to_dict()), 200

# Update Student
@app.route("/student/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "student not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "no input data"}), 400

    name = data.get("name")
    age = data.get("age")
    city = data.get("city")

    if name is not None:
        student.name = name
    if age is not None:
        student.age = age
    if city is not None:
        student.city = city

    db.session.commit()
    return jsonify(student.to_dict()), 200

# Delete Student
@app.route("/student/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "student not found"}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "deleted"}), 200

if __name__ == "__main__":
    # For local dev only; in production use gunicorn
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=os.environ.get("FLASK_DEBUG", "0") == "1")
