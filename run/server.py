from bottle import route, run, response
from json import dumps
from interpreter import interpret

# FUNCTION NAME <=====> ROUTE NAME
@route('/parse/<text>')
def parse(name=""):
        parsed = interpreter.parse(name.decode('unicode-escape'))
        response.content_type = "application/json"
        return dumps(parsed)

run(host='localhost', port=3000)
