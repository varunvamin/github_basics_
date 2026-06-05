from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/")
def abc():
    return "Thisis the ABC route."

if __name__=="__main__":
    app.run(debug=True)
