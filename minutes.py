# -*- coding: utf-8 -*-

from flask import Flask, \
                  render_template, \
                  request

from os import chmod, \
               getpid, \
               getppid
from shutil import copyfile
from time import time

from minutes_config import TITLE, \
                           CATEGORIES, \
                           SUBCATEGORIES, \
                           RESTRICT_BY_IP, \
                           IPS, \
                           HOST, \
                           PORT, \
                           DEBUG

app = Flask(__name__)

@app.route('/')
def index():
    if not RESTRICT_BY_IP or ( RESTRICT_BY_IP and request.remote_addr in IPS ):
        return render_template('minutes.html',
                               categories = CATEGORIES,
                               subcategories = SUBCATEGORIES,
                               title = TITLE)
    else:
        return "Access denied."

@app.route('/save', methods=['POST'])
def save_state():
    if not RESTRICT_BY_IP or ( RESTRICT_BY_IP and request.remote_addr in IPS ):
        try:
            state = request.form.get('state')
            state = state.encode('utf-8')
            f = open(".state", "w")
            f.write(state)
            f.close()
            return "1"
        except:
            print e
            return "0"

@app.route('/load', methods=['GET'])
def load_state():
    if not RESTRICT_BY_IP or ( RESTRICT_BY_IP and request.remote_addr in IPS ):
        try:
            f = open(".state", "r")
            state = f.read()
            state = state.decode('utf-8')
            f.close()
            chmod(".state", 0600)
            return state
        except:
            return "|||"

@app.route('/reset', methods=['GET'])
def reset_state():
    if not RESTRICT_BY_IP or ( RESTRICT_BY_IP and request.remote_addr in IPS ):
        try:
            version = str(time())
            copyfile(".state", ".state.%s" % (version,))
            chmod(".state.%s" % (version,), 0600)
            f = open(".state", "w")
            f.write("")
            f.close()
            chmod(".state", 0600)
            return "1"
        except:
            return "0"

def save_pid():
    try:
        pid = getpid()
        ppid = getppid()
        if ( ppid != 1 ):
            pid = ppid
        f = open(".pid", "w")
        f.write(str(pid))
        f.close()
        chmod(".pid", 0600)
    except:
        pass

if __name__ == '__main__':
    save_pid()
    app.debug = DEBUG
    app.run(host = HOST,
            port = PORT)

