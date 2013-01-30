from flask import Flask, \
                  render_template, \
                  request
from os import chmod, \
               getpid, \
               getppid
from shutil import copyfile
from time import time

# TODO:
#   * Write ./start and ./stop scripts

app = Flask(__name__)

TITLE = "DLS Section Meeting Minutes"
CATEGORIES = """ 
"E-Publishing",
"CDS",
"Invenio",
"Other",
"Outreach"
"""
SUBCATEGORIES = """ 
"Production",
"Support",
"Development",
"BlogForever",
"Outreach",
"CERN-2012-",
"CERN-2013-"
"""

IPS = ("127.0.0.1",
       "137.138.36.53",)

#HOST = "127.0.0.1"
HOST = "0.0.0.0"
#PORT = 5000
PORT = 1357 #1DLS
#DEBUG = True
DEBUG = False

@app.route('/')
def index():
    if request.remote_addr in IPS:
        return render_template('minutes.html',
                               categories = CATEGORIES,
                               subcategories = SUBCATEGORIES,
                               title = TITLE)
    else:
        return "Access denied."

@app.route('/save', methods=['POST'])
def save_state():
    if request.remote_addr in IPS:
        try:
            state = str(request.form.get('state'))
            f = open(".state", "w")
            f.write(state)
            f.close()
            return "1"
        except:
            return "0"

@app.route('/load', methods=['GET'])
def load_state():
    if request.remote_addr in IPS:
        try:
            f = open(".state", "r")
            state = str(f.read())
            f.close()
            chmod(".state", 0600)
            return state
        except:
            return "|||"

@app.route('/reset', methods=['GET'])
def reset_state():
    if request.remote_addr in IPS:
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

