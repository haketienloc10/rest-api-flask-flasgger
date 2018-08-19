from flask import Flask, request, jsonify, abort, Blueprint
from flask_pymongo import PyMongo, ObjectId
from database import mongo
from bson import json_util
import json

hello_bp = Blueprint('hello', __name__)


@hello_bp.route("/", methods=['GET'])
def getAllTask():
    tasks = mongo.db.tasks.find()
    res_js = json.loads(json_util.dumps(tasks))
    return jsonify(res_js)

@hello_bp.route("/<ObjectId:id>", methods=['GET'])
def getTask(id):
    tasks = mongo.db.tasks.find_one(id)
    if tasks == None:
        abort(404)
    res_js = json.loads(json_util.dumps(tasks))
    return jsonify(res_js)


@hello_bp.route("/", methods=['POST'])
def createTask():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    mongo.db.tasks.insert(task)
    res_js = json.loads(json_util.dumps(task))
    return jsonify(res_js), 201


@hello_bp.route("/<ObjectId:id>", methods=['PUT'])
def updateTask(id):
    task = mongo.db.tasks.find_one(id)
    if task == None:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' not in request.json:
        abort(400)
    if 'description' not in request.json:
        abort(400)
    if 'done' not in request.json and type(request.json['done']) is not bool:
        abort(400)
    task_update = {
        'title': request.json['title'],
        'description': request.json['description'],
        'done': request.json['done']
    }
    mongo.db.tasks.update_one(
        {'_id': id},
        {
            "$set": task_update
        }
    )
    task = mongo.db.tasks.find_one(id)
    res_js = json.loads(json_util.dumps(task))
    return jsonify(res_js)


@hello_bp.route("/<ObjectId:id>", methods=['DELETE'])
def deleteTask(id):
    task = mongo.db.tasks.find_one(id)
    if task == None:
        abort(404)
    mongo.db.tasks.remove({'_id': id})
    return jsonify({"result": True})


@hello_bp.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


@hello_bp.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400
