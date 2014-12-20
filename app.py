from flask import Flask

app = Flask (__name__)

@app.route("/")
@app.route("/hello")
def hello_world():
	return "Hello World!"

@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "Correct"

if __name__ == "__main__":
	app.run()