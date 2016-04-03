from django.http import HttpResponse
from django.http import FileResponse
from django.http import JsonResponse
from django.views.generic import View


class Controller(View):
    url_params = None

    """
    Base controller.
    """
    def html(self, data, template=None):
        """
        Send html document to user.

        Args:
        - data: Dict to render template, or string with rendered HTML.
        - template: Name of template to render HTML document with passed data.
        """
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
