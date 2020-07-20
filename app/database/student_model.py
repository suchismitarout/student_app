from app.database import db


class Student(db.Model):

    __tablename__ = "student"
    empid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    add = db.Column(db.Text)
    sal = db.Column(db.Integer)
    # dept_id = db.Column(db.Integer)
    dept_id = db.Column(db.Integer, db.ForeignKey('department.dept_id'))
    # dept = db.relationship('department', backref='student', lazy='dynamic')


    def __init__(self, name, age, add, empid, sal, dept_id):
        self.name = name
        self.age = age
        self.add = add
        self.empid = empid
        self.sal = sal
        self.dept_id = dept_id

    def __repr__(self):
        return "Emp_Id:{}, Name:{}, Age:{}, Add:{}, Sal:{}, Dept:{}".format(self.empid, self.name, self.age, self.add,
                                                                        self.sal, self.dept_id)

