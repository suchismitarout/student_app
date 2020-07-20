from flask import render_template, redirect, session, url_for, Blueprint
from app.api.department_form import DeptForm
import logging
from app.database.db_writer import DBWriter
from app.database.db_reader import DBReader

dept_route = Blueprint('department_api', __name__)

db_write = DBWriter()
db_read = DBReader()


@dept_route.route('/dept_register', methods=['GET', 'POST'])
def department_register():
    form = DeptForm()
    dept_info = {}
    if form.validate_on_submit():
        session["dept_id"] = form.dept_id.data
        session["dept_name"] = form.dept_name.data

        dept_info["Dept_id"] = int(session["dept_id"])
        dept_info["Dept_name"] = session["dept_name"]

        logging.debug(dept_info)
        db_write.insert_into_department(dept_info)
        logging.debug("inserted to department table")
        return redirect(url_for('department_api.view_dept_info'))
    return render_template('dept_form.html', form=form)


@dept_route.route('/getdept')
def get_student_data():
    return render_template('get_dept_info_by_dept_id.html')


@dept_route.route('/viewdept', methods=['GET', 'POST'])
def view_dept_info():
    form = DeptForm()
    if form.validate_on_submit():
        logging.debug("success")
        session['dept_id'] = form.dept_id.data
        logging.info(form.dept_id.data)
        dept_ob = db_read.read_by_dept(form.dept_id.data)
        logging.info(dept_ob.dept_name)
        session['dept_name'] = dept_ob.dept_name
        return redirect(url_for('department_api.get_student_data'))
    return render_template('view_student_by_dept_id.html', form=form)


@dept_route.route('/viewstudent', methods=['GET', 'POST'])
def view_student_by_deptid():
    form = DeptForm()
    if form.validate_on_submit():
        session['deptid'] = form.dept_id.data
        dept_ob = db_read.read_student_by_deptid(form.dept_id.data)
        logging.info(dept_ob)
        session['name'] = dept_ob.name
        session['age'] = dept_ob.age
        session['add'] = dept_ob.add
        session['sal'] = dept_ob.sal
        session['empid'] = dept_ob.empid
        return render_template('flask_form.html', form=form)
    return render_template('view_student_by_dept_id.html', form=form)
