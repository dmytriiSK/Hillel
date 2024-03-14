from flask import Flask, request
from faker import Faker

app = Flask(__name__)
fake = Faker()

@app.route('/generate_students')
def generate_students():
    count = request.args.get('count', default=1, type=int)
    count = min(count, 1000)
    students = []
    for _ in range(count):
        student = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(),
            'birthday': fake.date_of_birth(minimum_age=18, maximum_age=60)
        }
        students.append(student)

    # formatting students for output, testing HTML
    format_students = ""
    for student in students:
        format_students += f"<p>Name: {student['first_name']} {student['last_name']}<br>"
        format_students += f"Email: {student['email']}<br>"
        format_students += f"Password: {student['password']}<br>"
        format_students += f"Birthday: {student['birthday']}</p><br>"

    return format_students

