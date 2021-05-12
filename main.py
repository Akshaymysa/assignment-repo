import flask
import requests
import yaml

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/health', methods=['GET'])
def health():
    return "Healthy"

@app.route('/hello')
def summary():
    return {
           "response": "200"
        } 



app.run(host='0.0.0.0')
