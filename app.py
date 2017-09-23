from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	"""
	Initial setup for flask app
	:return:
	"""
	return "Hello World!"	

if __name__=='__main__':
	app.run(host='0.0.0.0', port=1003, debug=True, threaded=True)