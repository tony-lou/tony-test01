'''
Created on Jul 9, 2018

@author: louloulx
'''

from flask import Flask
import os

app = Flask(__name__)


@app.route("/hello", methods=['GET'])
def callback():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'])
