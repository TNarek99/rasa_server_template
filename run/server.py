from bottle import route, run, response
from json import dumps
from interpret import interpret

# FUNCTION NAME <=====> ROUTE NAME
@route('/parse/<text>')
def parse(text=""):
        parsed = interpret.parse(text.decode('unicode-escape'))
        response.content_type = "application/json"
        return dumps(parsed)

run(host='localhost', port=3000)
