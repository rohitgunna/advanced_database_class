<p>Edit an existing task in the ToDo list:</p>
<form action="/edit/{{id}}" method="POST">
  <input type="text" size="100" maxlength="100" name="task">{{text}}</input>
  <input type="submit" name="save" value="save">
</form>