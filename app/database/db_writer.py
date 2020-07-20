from app import db
import logging
from app.database.student_model import Student
from app.database.department_model import Department

class DBWriter():

    def insert_into_student(self, student_data):
        # db.create_all()
        student = Student(student_data['Name'], student_data['Age'], student_data['Address'], student_data['EmpId'], student_data['Salary'], student_data['DeptId'])
        db.session.add_all([student])
        db.session.commit()
        logging.debug("successfully inserted to student database")


    def insert_into_department(self, dept_data):

        dept = Department(dept_data['Dept_id'], dept_data['Dept_name'])
        db.session.add_all([dept])
        db.session.commit()
        logging.debug("successfully inserted into department database")
