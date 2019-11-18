from flask import Flask, render_template, jsonify, request
from random import *

app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")


@app.route('/api/run', methods=['GET'])
def test_run():
    text = str(request.args.get('input'))
    response = {
        'text1': text + " abc123"

    }
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
