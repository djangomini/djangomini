"""
Auto-discoverable urls.
"""
import re
from django.conf.urls import url
from django.contrib import admin
from .controllers import Controller
from .tools import import_module
from .tools import listdir


def auto_discover():
    """
    Auto-map urls from controllers directory.

    Ignored only files and classes that start from underscore.
    """
    urls = [
        url(r'^admin/', admin.site.urls),
    ]

    # TODO: we can create python package to have a lot of controllers
    # in separate files
    def get_controllers(module_name):
        """Return list of controllers in a module."""
        module = import_module('controllers.{}'.format(module_name))
        controllers = []
        for obj_name in dir(module):
            # we ignore import of Controller and hidden names
            if obj_name.startswith('_') or obj_name == 'Controller':
                continue
            obj = getattr(module, obj_name)
            # include only controllers
            if issubclass(obj, Controller):
                controllers.append(obj)
        return controllers

    def controller_to_path(controller):
        """
        Convert controller's name to a valid path.

        Make url in lower case by replace capital letters to small
        and adding underscore between words.
        """
        words = re.findall('[A-Z][a-z]*', controller.__name__)
        if words[-1] == 'Controller':
            del words[-1]
        # transform words to a url address
        url_path = '_'.join(words).lower()
        # main controller is a root handler
        # TODO: root address inside the file should always come last
        if url_path == 'main':
            url_path = ''
        return url_path

    # load all controllers (excluding main controllers)
    for file_name in listdir('controllers', get_files=True, hide_ignored=True):
        # remove .py extension from file name
        app_name = file_name.split('.', 1)[0]
        # we will include main controller at the end
        if app_name == 'main':
            continue
        # add url for each controller
        for controller in get_controllers(app_name):
            url_path = controller_to_path(controller)
            urls.append(url(
                r'^{}/{}$'.format(app_name, url_path),
                controller.as_view()
            ))

    # add urls for main controllers
    for controller in get_controllers('main'):
        url_path = controller_to_path(controller)
        # map urls to a root path
        urls.append(url(
            r'^{}$'.format(url_path),
            controller.as_view()
        ))

    return urls
