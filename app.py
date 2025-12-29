from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to my docker aws devops project"

app.run(host='0.0.0.0', port=5000)

