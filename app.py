import os

from http import HTTPStatus
from urllib import response

from flask import Flask
from dotenv import load_dotenv

env = load_dotenv()

app = Flask(__name__)

@app.route('/healthcheck/', methods=['GET'])
def health_check():  # put application's code here
    return {"status": "UP"}


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
