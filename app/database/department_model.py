from app.database import db


class Department(db.Model):

    __tablename__ = 'department'
    dept_id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.Text)

    dept = db.relationship('Student', backref='department', lazy='dynamic')

    def __init__(self, dept_id, dept_name):
        self.dept_id = dept_id
        self.dept_name = dept_name

