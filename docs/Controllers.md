# Controllers

In Django it called `Views`. We use more accurate name - Controllers.
By the way we included few helper methods into Controller class.
In the result of this improvement - you can write less code and that code looks more clear.

### New methods

In addition to Django View we have some additional methods.

#### `html(data, template=None)`

Send HTML document to user.

If `template` is passed - this template used to render HRML document with passed `data` dict.

#### `json(data)`

Send JSON document to user.

#### `file(filename)`

Send file to user. For example, it can be image or any file (PDF, DOc, etc).

#### `redirect(address)`

Redirect user to new page.
