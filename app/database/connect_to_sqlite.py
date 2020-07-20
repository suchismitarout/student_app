from app import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    add = db.Column(db.Text)
    empid = db.Column(db.Integer)
    sal = db.Column(db.Integer)

    def __init__(self, name, age, add, empid, sal):
        self.name = name
        self.age = age
        self.add = add
        self.empid = empid
        self.sal = sal

    def __repr__(self):
        return "student: Id={}, Name={}, Age={}, Add={}, Sal={}".format(self.empid, self.name, self.age, self.add,
                                                                        self.sal)
