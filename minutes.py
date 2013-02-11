#!/usr/bin/python
# -*- coding: utf-8 -*-

#########
# wemig #
#########

from flask import Flask, \
                  render_template, \
                  request

from os import chmod, \
               getpid, \
               getppid
from shutil import copyfile
from time import time

from minutes_config import TEMPLATE_CONFIGURATION, \
                           RESTRICT_BY_IP, \
                           IPS, \
                           HOST, \
                           PORT, \
                           DEBUG

# Instantiate the web application
app = Flask(__name__)

@app.route('/')
def index():
    """
    The web application main entry point.
    """

    if not RESTRICT_BY_IP or ( RESTRICT_BY_IP and request.remote_addr in IPS ):
        print TEMPLATE_CONFIGURATION
        return render_template('minutes.html',
                               **TEMPLATE_CONFIGURATION)
    else:
        return "Access denied."

@app.route('/save', methods=['POST'])
def save_state():
    """
    Save the current state to a local file.
    """

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
    """
    Load the last state from a local file.
    """

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
    """
    Version the current state in a local file and reset it.
    """

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
    """
    Get the process ID and store it in a local file.
    """

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
    # First, store the process ID
    save_pid()
    # Configure and start the web application with the given settings.
    app.debug = DEBUG
    app.run(host = HOST,
            port = PORT)

