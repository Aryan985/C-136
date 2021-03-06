from flask import Flask,jsonify,request
from data import data
api = Flask(__name__)
@api.route("/")
def info():
    return jsonify({
        "data":data      
    })
@api.route("/planet")
def pl_type():
    name = request.args.get("name")
    planetinfo = next(i for i in data if i["name"]==name)
    return jsonify({
        "data":planetinfo
    })
api.run()
