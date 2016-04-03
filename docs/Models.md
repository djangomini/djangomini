# Models

We added few useful additions to Django Models.

### Data validation with `validate_*` arguments

You can specify data validation in easy way when defining model `Field`. By default in Django Model Field you need to use `validators` property to pass a list of validators. In our implementation you need to pass extra properties with `validate_` prefix.

**Examples:**

```python
from djangotips.db import models

class UserModel(models.Model):
    # in addition to default max_length you can use validate_max
    name = models.CharField(validate_max=250)
    age = models.IntegerField(validate_min=18, validate_max=75)
    city = models.CharField(validate_choice=['CA', 'PL', 'UA', 'USA'])
```

As result this validation logic will be available in Django `ModelForm` instances.
