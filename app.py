#==============================================================================
# Title:                app.py
# Description:          This is the logic of the Mrs Miggins vote app using
#                       Python and specifically flask.
#
# Author:          		Rob Edwards (@clijockey)
# Date:                 01/02/17
# Version:              0.5
# Notes:                This uses https://github.com/docker/example-voting-app
#                       as a base for the app and customised for my requirements
# Limitations/issues:
#==============================================================================

from flask import Flask, render_template, request, make_response, g
#from redis import Redis
import os
import socket
import random
import json

# The options availble to be voted on
option_a = os.getenv('OPTION_A', "El Salvador")
option_b = os.getenv('OPTION_B', "Rwanda")
hostname = socket.gethostname()

app = Flask(__name__)
port = int(os.getenv("PORT"))

def get_redis():
    '''
    xxxxxx
    
    '''
    if not hasattr(g, 'redis'):
        g.redis = Redis(host="redis", db=0, socket_timeout=5)
    return g.redis

@app.route("/", methods=['POST','GET'])

def hello():
    '''
    xxxxxx
    :param xx: xxx
    :param xx: xxx
    :return: xxx
    '''
    voter_id = request.cookies.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]

    vote = None

    if request.method == 'POST':
        redis = get_redis()
        vote = request.form['vote']
        data = json.dumps({'voter_id': voter_id, 'vote': vote})
        redis.rpush('votes', data)

    resp = make_response(render_template(
        'index.html',
        option_a=option_a,
        option_b=option_b,
        hostname=hostname,
        vote=vote,
    ))
    resp.set_cookie('voter_id', voter_id)
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
    #app.run(host='0.0.0.0', port=port, debug=True, threaded=True)


