from bottle import route, run, request

import parser

@route('/calc/<expression>')
def hello(expression):
    return {'expression':expression, 'value':parser.parse(expression)}

run(host='localhost', port=8080)