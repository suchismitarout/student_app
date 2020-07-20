from flask import render_template, redirect, session, url_for, Blueprint
from app.api.student_form import InfoForm
import logging
from app.database.db_writer import DBWriter
from app.database.db_reader import DBReader

student_route = Blueprint('student_api', __name__)

logging.basicConfig(level=logging.DEBUG)

logging.debug("hello")

db_write = DBWriter()
db_read = DBReader()


@student_route.route('/register', methods=['GET', 'POST'])
def student_register():
    form = InfoForm()
    logging.debug("instance of infoform created")
    student_info = {}
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['age'] = form.age.data
        session['add'] = form.add.data
        session['empid'] = form.empid.data
        session['sal'] = form.sal.data
        session['dept_id'] = form.dept_id.data
        student_info['Name'] = session['name']
        student_info['Age'] = int(session['age'])
        student_info['Address'] = session['add']
        student_info['EmpId'] = int(session['empid'])
        student_info['Salary'] = int(session['sal'])
        student_info['DeptId'] = int(session['dept_id'])
        logging.debug(student_info)

        db_write.insert_into_student(student_info)
        ## TODO: work on imprvoving based on result.
        return redirect(url_for('student_api.thank_you'))
    return render_template('reg_form.html', form=form)


@student_route.route('/thankyou')
def thank_you():
    return render_template('flask_form.html')


@student_route.route('/view', methods=['GET', 'POST'])
def view_by_id():
    form = InfoForm()
    if form.validate_on_submit():
        logging.debug("success")
        session['empid'] = form.empid.data
        logging.debug(form.empid.data)
        student_ob = db_read.read(form.empid.data)
        logging.debug(student_ob)
        logging.info(dir(student_ob))
        logging.info(type(student_ob))

        session['name'] = student_ob.name
        session['age'] = student_ob.age
        session['add'] = student_ob.add
        session['sal'] = student_ob.sal
        session['dept_id'] = student_ob.dept_id
        return redirect(url_for('student_api.thank_you'))
    return render_template('view_student_by_id.html', form=form)

# if __name__ == '__main__':
#     app.run()
