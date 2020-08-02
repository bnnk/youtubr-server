from flask_sqlalchemy import SQLAlchemy
from flask_whooshalchemy import whoosh_index as whooshify

rdbms = None
def setapp(app_):
    global rdbms
    app = app_
    rdbms = SQLAlchemy(app)
    class YoutubrAPIData(rdbms.Model):
            __searchable__ = ["author","title","description","date"]
            author = rdbms.Column(rdbms.String(10000), primary_key=True)
            vid = rdbms.Column(rdbms.String(10000))
            title = rdbms.Column(rdbms.String(10000))
            url = rdbms.Column(rdbms.String(10000))
            thumbnail = rdbms.Column(rdbms.String(10000))
            description = rdbms.Column(rdbms.String(10000))
            date = rdbms.Column(rdbms.String(10000))
            views = rdbms.Column(rdbms.String(10000))
            comments = rdbms.Column(rdbms.String(10000))
            ch = rdbms.Column(rdbms.String(10000))
            def __repr__(self):
                return '<YoutubrVideo %r>' % self.vid
    whooshify(app, YoutubrAPIData)
    return rdbms,YoutubrAPIData