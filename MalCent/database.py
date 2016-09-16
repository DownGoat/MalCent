__author__ = 'sis13'

from MalCent import app, foo
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql://%s:%s@%s/%s" % (app.config["DB_USER"], app.config["DB_PASS"],
                                                app.config["DB_HOST"], app.config["DB_NAME"]), convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
    autoflush=False,
    bind=engine))

Model = declarative_base()
Model.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import MalCent.models.queue
    import MalCent.models.report
    import MalCent.models.filename

    Model.metadata.create_all(bind=engine)