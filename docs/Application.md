Application structure
==========

Application structure is very simplified compared to Django project.
We don't have support of Django pluggable applications, and you will see that it can simplify your life a lot.

### Project structure looks like this

```sh
myapplication/
..controllers/    # django views renamed to controllers
....blogs.py
....main.py
....polls.py
..models/
....blogs.py
....polls.py
....users.py
..templates/
....blogs/
....polls/
..urls.py         # framework detects new controllers and you can use it without defining new url pattern
..wsgi.py
..settings.py
```

Later you will see that we use `from djangomini import ...` to use extended functionality.
