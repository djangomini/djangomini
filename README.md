# Django(mini)

### Infrastructure for rapid development on Django

This project is a layer over the [Django](http://djangoproject.com) web framework. We made some improvements, but all what you love in the original **Django** - remains. You can use it as you like, but you can save a lot of your valuable time by using some of our tools to have more fun when you developing your new web application,

### Some features

- **auto-discovered urls** - you don't need to describe urls in the `urls.py`
- **simplified project structure** with **no apps**. Forget about questions like this: *"Where to place this new model class?"*
- **improved models** allows to write less code and speed-up development
- all our code based on the **latest version of Django** framework *(from 1.9.x and up)*

Read our **[full documentation](docs)**.

## Run test project

We have prepared a test project to help you play with Django(mini).

### Use stable version

If you need to install stable version - run this command: `pip install -U djangomini` (`-U` used to upgrade previously installed version).

- `mkdir ~/workspace && cd ~/workspace`
- `git clone git@github.com:djangomini/new_project.git`
- `mkvirtualenv djangomini --python=$(which python3)`
- `cd new_project`
- `pip install -U -r requirements.txt`
- `python manage.py runserver`

### Use development version

If you need to checkout development version and play with it.

- do all as described above, but comment line with `djangomini` in `requirements.txt`. We need to use our local copy of `djangomini`
- `mkdir ~/workspace && cd ~/workspace`
- `git clone git@github.com:djangomini/djangomini.git`
- `cd ~/.virtualenvs/djangomini/lib/python3.5/site-packages/`
- `ln -s ~/workspace/djangomini/djangomini .` - it will create a symlink to a cloned project. You can change files and changes appear automatically in your test project that used `djangomini`
- `cd ~/workspace/new_project`
- `./manage.py runserver`

-------

Made with ♥️ Love to web development. | Project stats on [pypi](https://pypi.python.org/pypi/djangomini)
