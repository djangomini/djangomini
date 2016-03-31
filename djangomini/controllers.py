from django.http import HttpResponse
from django.views.generic import View


class Controller(View):
    url_params = None

    """
    Base controller.
    """
    def send(self, data):
        return HttpResponse(data)
