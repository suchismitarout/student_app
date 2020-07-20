from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField
from wtforms.validators import DataRequired

class InfoForm(FlaskForm):

    name = StringField("Name")
    age = StringField("Age")
    add = StringField("Address")
    empid = StringField("EmpId")
    sal = StringField("Salary")
    dept_id = StringField("DeptId")
    submit = SubmitField("Submit")



