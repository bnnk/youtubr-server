# Write your code here :-)
from flask import Flask,request
from flask_restful import Resource, Api
from model import *
from os import getcwd
from datasetmaker import VID2Info
build_with_se
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" +
app.logger.info("Started Youtubr Server")
rdbms,YoutubrAPIData = setapp(app)
api = Api(app)
rdbms.create_all()
ifo = VID2Info("YOUTUBE_DATA_API_KEY_HERE")

class Help(Resource):
    def get(self):
        return {'search': 'POST /api/v3/search',
        'all': 'GET /api/v3/all',
        'insert' : 'POST /api/v3/insert',
        'get' : 'GET /api/v3/get/<video-id>',
        'file': '/api/v3/file',
        'search-youtube':'/api/v3/search-youtube'}
class Search(Resource):
    def post(self):
        re = YoutubrAPIData.query.whoosh_search(request.get_json()["query"]).all()
        out = []
        for obj in re:
           out.append({
                'Author': obj.author,
                "Title": obj.title,
                "Video ID" : obj.title,
                'URL': obj.url,
                'Thumbnail': obj.thumbnail,
                "Description": obj.description,
                "Published Date": obj.date,
                "Views": obj.views,
                "Comments": obj.comments,
                "Channel ID": obj.ch
            })
        return out
class All(Resource):
    def get(self):
        re = YoutubrAPIData.query.all()
        out = []
        for obj in re:
           out.append({
                'Author': obj.author,
                "Title": obj.title,
                "Video ID" : obj.title,
                'URL': obj.url,
                'Thumbnail': obj.thumbnail,
                "Description": obj.description,
                "Published Date": obj.date,
                "Views": obj.views,
                "Comments": obj.comments,
                "Channel ID": obj.ch
            })
        return out
class Get(Resource):
    def post(self,id_):
        re = YoutubrAPIData.query.filter_by(vid=id_).all()
        out = []
        for obj in re:
           out.append({
                'Author': obj.author,
                "Title": obj.title,
                "Video ID" : obj.title,
                'URL': obj.url,
                'Thumbnail': obj.thumbnail,
                "Description": obj.description,
                "Published Date": obj.date,
                "Views": obj.views,
                "Comments": obj.comments,
                "Channel ID": obj.ch
            })
        return out
class Insert(Resource):
    def post(self):
        obj = YoutubrAPIData(**ifo.build(request.get_json()["id"]))
        rdbms.session.add(obj)
        rdbms.session.commit()
        out = {
            'Author': obj.author,
            "Title": obj.title,
            "Video ID" : obj.title,
            'URL': obj.url,
            'Thumbnail': obj.thumbnail,
            "Description": obj.description,
            "Published Date": obj.date,
            "Views": obj.views,
            "Comments": obj.comments,
            "Channel ID": obj.ch
        }
        return out
class File(Resource):
    def get(self):
        return sendfile(getcwd() + "/model.db")
class SearchYoutube(Resource):
    def post(self):
        out = []
        for dat in ifo.build_with_se(request.get_json()["kw"]):
            obj = YoutubrAPIData(**dat)
            rdbms.session.add(obj)
            out.append({
                'Author': obj.author,
                "Title": obj.title,
                "Video ID" : obj.title,
                'URL': obj.url,
                'Thumbnail': obj.thumbnail,
                "Description": obj.description,
                "Published Date": obj.date,
                "Views": obj.views,
                "Comments": obj.comments,
                "Channel ID": obj.ch
            })
        rdbms.session.commit()
        return out
api.add_resource(Help, '/api/v3')
api.add_resource(All, '/api/v3/all')
api.add_resource(Search, '/api/v3/search')
api.add_resource(Get, '/api/v3/get/<id_>')
api.add_resource(Insert, '/api/v3/insert')
api.add_resource(File, '/api/v3/file')
api.add_resource(SearchYoutube, '/api/v3/search-youtube')

if __name__ == '__main__':
    setapp(app)
    app.run(host="localhost",port="4040")