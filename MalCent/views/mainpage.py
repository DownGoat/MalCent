__author__ = 'sis13'

from flask import *


mod = Blueprint('mainpage', __name__)

@mod.route("/")
def index():
    return render_template("mainpage.html")

