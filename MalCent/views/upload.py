__author__ = 'sis13'

from flask import *
import MalCent.checksums
from MalCent.error_codes import *
from MalCent.utils import *
from MalCent import app
from MalCent.database import db_session
from MalCent.models.queue import Queue
from MalCent.models.report import Report
from MalCent.models.filename import Filename
from datetime import datetime
import os

mod = Blueprint('upload', __name__)

@mod.route("/upload", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']

        sha1 = MalCent.checksums.sha1(file.read())

        q = Queue.query.filter(Queue.sha1 == sha1).first()
        if q:
            return redirect(url_for('analysis.analysis', sha1=sha1))

        r = Report.query.filter(Report.sha1 == sha1).first()
        if r:
            found = False
            fnames = Filename.query.filter(Filename.sample_id == r.id)
            for f in fnames:
                if f.filename == file.filename:
                    found = True

            if not found:
                f = Filename(r.id, file.filename)
                db_session.add(f)

            r.last_seen = datetime.utcnow()
            db_session.add(r)
            db_session.commit()
            return redirect(url_for('analysis.analysis', sha1=sha1))

        file.seek(0)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], sha1))

        q = Queue(sha1, file.filename, file.tell())
        db_session.add(q)
        db_session.commit()

        return render_template("queue.html", domain=app.config["DOMAIN"], sha1=sha1, number=len(Queue.query.all()))

@mod.route("/upload/url", methods=["POST"])
def upload_from_url():
    print(request.form["url"])
