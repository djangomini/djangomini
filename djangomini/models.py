from django.db import models
from django.shortcuts import get_object_or_404


class Model(models.Model):
    """
    Base model class.
    """

    @classmethod
    def get_object_or_404(cls, *args, **kwargs):
        """
        Return requested Model's object or return 404 error.
        """
        return get_object_or_404(cls, *args, **kwargs)
