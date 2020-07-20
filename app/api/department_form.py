from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField
from wtforms.validators import DataRequired

class DeptForm(FlaskForm):

    dept_id = StringField("Dept_Id")
    dept_name = StringField("Dept_Name")
    submit = SubmitField("Submit")