import logging
from app.database.student_model import Student
from app.database.department_model import Department

logging.basicConfig(level=logging.DEBUG)


class DBReader():

    def read(self, student_eid):
        return Student.query.filter_by(empid=student_eid).first()

    def read_by_dept(self, department_id):
        return Department.query.filter_by(dept_id=department_id).first()

    def read_student_by_deptid(self, department_id):
        return Student.query.filter_by(dept_id=department_id).first()

    def read_students_by_deptid(self, department_id):
        return Student.query.filter_by(dept_id=department_id).all()
