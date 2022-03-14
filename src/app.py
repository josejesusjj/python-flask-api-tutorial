from flask import Flask, jsonify, request
import json

app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": True }
]

    #Retrieving all items:
@app.route('/todos', methods=['GET'])
def todo_list():
    return jsonify(todos)

    #creating an item:
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_data = request.data
    decoded_object = json.loads(request_data)
    print("Incoming request with the following body", request_data)
    todos.append(decoded_object)
    return jsonify(todos)

    #erasing an item:
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)