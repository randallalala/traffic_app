import os
from flask import Flask
from redis import Redis

app = Flask(__name__)
# redis = Redis(host='redis', port=6379)
redis = Redis(host='localhost', port=6379) 

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'This is the %s visitor.' % count

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

