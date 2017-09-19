import sqlite3
from bottle import route, run, template, debug, request

@route('/')
@route('/index.html')
@route('/tasks')
def tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('current_tasks', rows=result)
    return output

@route('/new', method='GET')
def new():
    return template('new_task')    

@route('/new', method='POST')
def new_item():
    new = request.POST.task.strip()

    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
    new_id = c.lastrowid

    conn.commit()
    c.close()

    return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id

debug(True)
run(host='localhost', port=8080)