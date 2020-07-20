import logging
from app.database.connect_to_sqlite import Student


logging.basicConfig(level=logging.DEBUG)


class DBReader():

    def read(self, student_eid):
        return Student.query.filter_by(empid=student_eid).first()




