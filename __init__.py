from flask import Flask, jsonify
# import json
from .file2 import ClassB
app = Flask(__name__)

cb = ClassB()
hello = cb.methodB()
# print("hey=",hello)
# print(type(hello))
hell = {'Greeting':hello}

@app.route('/')
def hello():
	return jsonify(hell)



# if __name__ == '__main__':
#     app.run(debug=True)