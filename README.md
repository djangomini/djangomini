# Django(mini)

### Infrastructure for rapid development on Django

This project is a `@decorator` over the [Django](http://djangoproject.com) web framework. We made some improvements, but all what you love in the original **Django** - remains. You can use it as you like, but you can save a lot of your valuable time by using some of our tools to have more fun when you developing your new web application,

### Some features

- **auto-discovered urls** - you don't need to describe urls in the `urls.py`
- **simplified project structure** with **no apps**. Forget about questions like this: *"Where to place this new model class?"*
- **improved models** allows to write less code and speed-up development
- all our code based on the **latest version of Django** framework *(from 1.9.x and up)*

Read our **documentation** on [wiki](//github.com/djangomini/djangomini/wiki) pages.

### Development version

If you need to checkout development version and play with it.

- `mkdir ~/workspace && cd ~/workspace`
- `git clone git@github.com:djangomini/djangomini.git`
- `mkvirtualenv djangomini --python=$(which python3)`
- `cd ~/.virtualenvs/djangomini/lib/python3.5/site-packages/`
- `ln -s ~/workspace/djangomini/djangomini .` - it will create a symlink to a cloned project. You can change files and changes affected automatically
- `cd ~/workspace/djangomini/test_project`
- `./manage.py runserver`

-------

Made with ♥️ Love to web development.
