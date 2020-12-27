from flask import Flask, jsonify
# import json
from .file2 import ClassB
app = Flask(__name__)


# print("hey=",hello)
# print(type(hello))


@app.route('/')
def hello():
	cb = ClassB()
	hello = cb.methodB()
	hell = {'Greeting':hello}
	return jsonify(hell)



# if __name__ == '__main__':
#     app.run(debug=True)