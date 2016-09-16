from flask import *

foo = "bar"
app = Flask(__name__)
app.config.from_object('config')

app.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename=filename))

@app.route("/family")
def family():
    return render_template("family.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

from MalCent import checksums
from MalCent.error_codes import  *
from MalCent.views import upload
from MalCent.views import analysis
from MalCent.views import mainpage
from MalCent.database import db_session
app.register_blueprint(upload.mod)
app.register_blueprint(analysis.mod)
app.register_blueprint(mainpage.mod)

if __name__ == '__main__':
    app.run(debug=True)
