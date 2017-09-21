from bottle import route, run, request

import parser

@route('/calc/')
@route('/calc/<expression>')
def evaluate(expression=""):
    print(expression)
    value = parser.parse(expression)
    print(value)
    if value == None:
        value = '#NONE#'
    return {'expression':expression, 'value':value}

run(host='localhost', port=8080)