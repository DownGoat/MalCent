__author__ = 'sis13'

from flask import *
from MalCent.models.report import Report
from MalCent.models.queue import Queue
from MalCent.models.filename import Filename
from MalCent import app


mod = Blueprint('analysis', __name__)

@mod.route("/analysis/<sha1>")
def analysis(sha1):
    q = Queue.query.filter(Queue.sha1 == sha1).first()
    if q:
        qa = Queue.query.all()
        n = 1

        for x in qa:
            if q == x:
                break

            n += 1

        return render_template("allready_queued.html", domain=app.config["DOMAIN"], sha1=sha1, number=n)

    r = Report.query.filter(Report.sha1 == sha1).first()

    if not r:
        return redirect(url_for('mainpage.index'))

    fnames = Filename.query.filter(Filename.sample_id == r.id).all()

    return render_template("report.html", r=r, name=fnames[0], fnames=fnames)
