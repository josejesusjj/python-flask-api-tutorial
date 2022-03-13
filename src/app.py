from flask import Flask, jsonify, request
import json

app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": True }
]

    #Retornando la lista de items:
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

    #creando un item:
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_data = request.data
    decoded_object = json.loads(request_data)
    print("Incoming request with the following body", request_data)
    todos.append(decoded_object)
    return jsonify(todos)


    #retornando un item:
#@app.route('todos/<int:id_item>', methods=['GET'])
#def get_item(id_item):
#    item = {}
#    for element in todos:
#        if element.get('id') == id_item:
#            item = element
#    return jsonify(item)

    #primeros tests:
#@app.route('/todos', methods=['GET'])
#def hello_world():
#    return "<h1>Hello!</h1>"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)