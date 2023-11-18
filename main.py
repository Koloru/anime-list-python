import os

from dotenv import load_dotenv
from flask import Flask, abort, jsonify, request

from config.db import create_tables

load_dotenv()

app = Flask(__name__)

create_tables()
methods = os.getenv('ALLOWED', ['GET'])


@app.before_request
def check_request():
    if request.method not in methods:
        return {'message': '405 Method Not Allowed'}


@app.route("/api/anime/create", methods=['POST'])
def handle_create():
    return jsonify({'Hello': 'POST!'})


if __name__ == '__main__':
    app.run(debug=True)
