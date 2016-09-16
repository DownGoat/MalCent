import datetime

__author__ = 'sis13'

from MalCent.database import db_session
from MalCent import app
from MalCent.checksums import *
from MalCent.models.queue import Queue as _Queue
from MalCent.models.report import Report
from MalCent.models.filename import Filename
from datetime import datetime
import os, time
import threading, Queue

while True:
    queue = _Queue.query.all()
    if not queue:
        print("Sleep")
        time.sleep(1)
        continue

    queue = queue[0]

    sums = checksums(os.path.join(app.config['UPLOAD_FOLDER'], queue.sha1))

    r = Report(sums["sha1"], sums["sha256"], sums["md5"], sums["ssdeep"], datetime.utcnow(), datetime.utcnow(), queue.filesize)



    db_session.add(r)
    db_session.delete(queue)
    db_session.commit()

    r = Report.query.filter(Report.sha1 == queue.sha1).first()
    f = Filename(r.id, queue.filename)
    db_session.add(f)
    db_session.commit()