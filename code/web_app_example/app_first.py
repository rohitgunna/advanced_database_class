from bottle import route, run, template, request

@route('/hello')
def hello():
    return template("<b>Hello, {{name}}!</b>", name="Database Class")

@route('/hello/<your_name>')
def hello_name(your_name):
    print(dict(request.query))
    if int(request.query.caps) > 0:
        your_name = your_name.upper()
    tag1 = ""
    tag2 = ""
    if int(request.query.italics) > 0:
        tag1 = "<i>"
        tag2 = "</i>"
    return template("{{tag1}}<b>Hello, {{name}}!</b>{{tag2}}", 
                    name=your_name,
                    tag1=tag1,
                    tag2=tag2)

run(host='localhost', port=8080, reloader=True)