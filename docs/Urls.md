# Urls

In Django project you need to define a list of url addresses and appropriate view handlers. And you can find that when your application grows - your urls don't match name conventions with view handlers. This creates problem with understanding the project and opens a doors for new bugs.

### Project development cycle

- teach `urls.py` to automatically detect new controllers *(see code below)*
- create new python file inside `controllers` directory to define request handlers *(like `polls.py`)*. If you need to make this controller hidden - rename it with leading underscore *(like `_polls.py`)*
- inside `controllers/polls.py` create one or more classes (like this `AddPollController`, see code below)*. To make this controller hidden - add leading underscore to the class name
- you can access your new page by address: `/polls/add_poll`

**Note.** To handle **empty** url *(like homepage)* you need to create `MainController` that handle this type of requests *(requests to root page)*.

### Example of `urls.py`

```python
from djangomini.urls import auto_discover

urlpatterns = auto_discover()
```

### Example of `controllers/polls.py`

```python
from djangomini.controllers import Controller

class AddPollController(Controller):
    """Create new Poll object."""

    def get(self, request):
        return self.send('Create new poll (show form).')

    def post(self, request):
        return self.send('Create new poll (handle POST request).')
```
