from flask import Flask, jsonify, request
import json
app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": True }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'
 
#@app.route('/todos', methods=['GET'])
#def hello_world():
#    return "<h1>Hello!</h1>"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)