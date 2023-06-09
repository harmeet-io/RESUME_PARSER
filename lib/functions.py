
from django.db import models
from uuid import uuid4


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key = True, editable = False, unique = True, default = uuid4 )

    class Meta:
        abstract = True


def get_file_path(instance, filename):
    return 'files/{0}/{1}'.format(instance.user.id, filename)




