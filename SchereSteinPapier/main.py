import requests
from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
import json
from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass

Base = declarative_base()
metadata = Base.metadata
engine = create_engine(r'sqlite:///C:\temp\statistics.sqlite3')
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
Base.query = db_session.query_property()

app = Flask(__name__)
app.secret_key = '5#y2L”F4Q8z\e]/'
api = Api(app)


@dataclass
class GameStats(Base):
    __tablename__ = 'stats'
    id: int
    schere: int
    stein: int
    papier: int
    echse: int
    spock: int
    spielerW: int
    compW: int
    unentschieden: int

    id = Column(Integer, primary_key=True)
    schere = Column(Integer)
    stein = Column(Integer)
    papier = Column(Integer)
    echse = Column(Integer)
    spock = Column(Integer)
    spielerW = Column(Integer)
    compW = Column(Integer)
    unentschieden = Column(Integer)

class Services(Resource):
    def get(self, id):
        info = GameStats.query.get(id)
        if info is None:
            return jsonify({'message': 'player does not exist'})
        return jsonify(info)

    def delete(self, id):
        info = GameStats.query.get(id)
        db_session.delete(info)
        db_session.flush()
        return jsonify({'message': '%d deleted' % id})

    def put(self,id):
        data = request.get_json(force=True)['info']
        info = GameStats(schere=data['schere'], stein=data['stein'], papier=data['papier'], echse=data['echse'], spock=data['spock'], spielerW=data['spielerW'], compW=data['compW'], unentschieden=data['unentschieden'])
        db_session.add(info)
        db_session.flush()
        obj = GameStats.query.all()
        return obj[-1].id

    def patch(self, id):
        info = GameStats.query.get(id)
        if info is None:
            return jsonify({'message': 'stats does not exist'})
        data = json.loads(request.form['info'])
        if 'schere' in data:
            info.schere = data['schere']
        if 'stein' in data:
            info.stein = data['stein']
        if 'papier' in data:
            info.papier = data['papier']
        if 'echse' in data:
            info.echse = data['echse']
        if 'spock' in data:
            info.spock = data['spock']
        if 'spielerW' in data:
            info.spielerW = data['spielerW']
        if 'compW' in data:
            info.compW = data['compW']
        if 'unentschieden' in data:
            info.unentschieden = data['unentschieden']
        db_session.add(info)
        db_session.flush()
        return jsonify({'message': 'stats with id %d modified' % id})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<id>')
def stats(id):
    response = requests.get("http://127.0.0.1:5000/stats/%s"%id)
    r = response.json()
    i =[r]
    return render_template("stats.html",stats=i)

api.add_resource(Services, '/stats/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)