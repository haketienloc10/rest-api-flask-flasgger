from flask import Flask, request, jsonify, abort, Blueprint
from flask_pymongo import PyMongo, ObjectId
from database import mongo
from bson import json_util
import json
from flasgger.utils import swag_from
from flasgger import Swagger
from document import getTask_dict, getAllTask_dict, createTask_dict, updateTask_dict,deleteTask_dict

from flask_httpauth import HTTPBasicAuth

hello_bp = Blueprint('hello', __name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'tienloc':
        return '123'
    return None

@auth.error_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized access'}), 401

@hello_bp.route("/", methods=['GET'])
@swag_from(getAllTask_dict)
# @auth.login_required
def getAllTask():
    tasks = mongo.db.tasks.find()
    res_js = json.loads(json_util.dumps(tasks))
    return jsonify(res_js)

@hello_bp.route("/<ObjectId:id>", methods=['GET'])
# @auth.login_required
@swag_from(getTask_dict)
def getTask(id):
    tasks = mongo.db.tasks.find_one(id)
    if tasks == None:
        abort(404)
    res_js = json.loads(json_util.dumps(tasks))
    return jsonify(res_js)


@hello_bp.route("/", methods=['POST'])
# @auth.login_required
@swag_from(createTask_dict)
def createTask():
    print(not request.json or not 'title' in request.json)
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
# @auth.login_required
@swag_from(updateTask_dict)
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
# @auth.login_required
@swag_from(deleteTask_dict)
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
