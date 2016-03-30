from queue.celery import app
from queue import models


@app.task()
def add_to_queue(uuid):
    models.Queue.objects.create(uuid=uuid)
