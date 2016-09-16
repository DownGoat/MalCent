__author__ = 'sis13'

from flask import render_template
from MalCent import app
import MySQLdb


def create_error(code):
    return render_template('error.html', code=code, contact=app.config['CONTACT_EMAIL'])
