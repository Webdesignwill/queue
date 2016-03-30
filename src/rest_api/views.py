import uuid
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, list_route
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_api import serializers
from queue import models, tasks


@api_view(('GET',))
def api_root(request, version, format=None):
    return Response({
        'version': '1.0',
        'queue': reverse('rest_api:queue-list', request=request, kwargs={'version': version}),
    })


class QueueViewSet(
        ListModelMixin,
        RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Queue.objects.all()
    serializer_class = serializers.QueueSerializer
    lookup_field = 'uuid'

    @list_route(methods=['post'])
    def get_ticket(self, request, *args, **kwargs):
        cookie_value = str(uuid.uuid4())
        tasks.add_to_queue.apply_async(args=[cookie_value])
        return Response(
            {'uuid': cookie_value},
            status=status.HTTP_201_CREATED
        )
