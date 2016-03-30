import datetime
import uuid
from django.db import models


class Queue(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    @property
    def rank(self):
        """
        returns which rank the current Queue object is in
        """
        one_minute_ago = datetime.datetime.now() - datetime.timedelta(minutes=15)
        return Queue.objects.filter(created__lte=self.created, created__gte=one_minute_ago).count()
