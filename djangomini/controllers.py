from django.http import HttpResponse
from django.http import FileResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View


class Controller(View):
    """
    Base controller.

    Main difference from Django's View is that 'request' isn't
    passed to a Controller's method call.
    """

    request = None
    url_params = None

    def dispatch(self, request, *args, **kwargs):
        """
        Redefine parent's method.

        Main difference between Django's approach and ours - we don't push
        a 'request' to a method call. We use 'self.request' instead.
        """
        # this part copied from django source code
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(),
                              self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        # we changed only this line - removed first 'request' argument
        return handler(*args, **kwargs)

    def html(self, data, template=None):
        """
        Send html document to user.

        Args:
        - data: Dict to render template, or string with rendered HTML.
        - template: Name of template to render HTML document with passed data.
        """
        if template:
            return render(self.request, template, data)
        return HttpResponse(data)

    def json(self, data):
        """
        Send json document to user.

        Args:
        - data: Dict that converts to JSON object.
        """
        return JsonResponse(data)

    def file(self, filename):
        """
        Send file to user.

        Used to send any file: image, document (PDF, DOC), etc.

        Args:
        - filename: Path to file that we need to send
        """
        return FileResponse(open(filename, 'rb'))

    def redirect(self, address):
        """
        Redirect user to new page.

        Args:
        - address: Can be a string with url address, or Model object that
          implements 'get_absolute_url()' method.
        """
        return redirect(address)


class ViewObjectController(Controller):
    pass


class ViewObjectListController(Controller):
    pass


class CreateObjectController(Controller):
    pass


class EditObjectController(Controller):
    pass


class DeleteObjectController(Controller):
    pass
