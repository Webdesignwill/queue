from rest_framework import serializers

from queue import models


class QueueSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Queue
        fields = ('uuid', 'created', 'rank')
