from app import db
import logging
from app.database.connect_to_sqlite import Student

class DBWriter():

    def insert(self, student_data):
        # db.create_all()
        student = Student(student_data['Name'], student_data['Age'], student_data['Address'], student_data['EmpId'], student_data['Salary'])
        db.session.add_all([student])
        db.session.commit()
        logging.debug("successfully inserted to database")
