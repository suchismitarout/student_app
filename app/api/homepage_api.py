from flask import render_template, Blueprint
import logging


home_route = Blueprint('home_api', __name__)

logging.basicConfig(level=logging.DEBUG)


@home_route.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home_page.html')