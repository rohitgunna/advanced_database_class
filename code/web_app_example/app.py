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

@route('/complete/<id>', method='GET')
def complete(id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE todo SET status = 0 WHERE id LIKE ?", (id,))

    conn.commit()
    c.close()

    return '<p>The new task was marked complete in the database, the ID is %s</p>' % id

@route('/delete/<id>', method='GET')
def delete(id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE from todo WHERE id LIKE ?", (id,))

    conn.commit()
    c.close()

    return '<p>The new task was deleted from the database, the ID is %s</p>' % id



debug(True)
run(host='localhost', port=8080)