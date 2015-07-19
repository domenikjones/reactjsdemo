from rest_framework import viewsets
from rest_framework import generics

from apiv1.serializers import AppartementSerializer, AppartementTypeSerializer
from demo.models import Appartement, AppartementType


class AppartementList(generics.ListAPIView):
    serializer_class = AppartementSerializer

    def get_queryset(self):
        """
        This view should return a list of filtered appartement objects
        :return:
        """
        filters = {}

        # price range
        if self.request.GET.get('price_from'):
            filters['price__gte'] = self.request.GET.get('price_from')
        if self.request.GET.get('price_to'):
            filters['price__lte'] = self.request.GET.get('price_to')

        # rooms range
        if self.request.GET.get('room_from'):
            filters['rooms__gte'] = self.request.GET.get('room_from')
        if self.request.GET.get('room_to'):
            filters['rooms__lte'] = self.request.GET.get('room_to')

        # living_space range
        if self.request.GET.get('living_space_from'):
            filters['living_space__gte'] = self.request.GET.get('living_space_from')
        if self.request.GET.get('living_space_to'):
            filters['living_space__lte'] = self.request.GET.get('living_space_to')

        return Appartement.objects.published(filters=filters)


class AppartementViewSet(viewsets.ModelViewSet):
    queryset = Appartement.objects.visible()
    serializer_class = AppartementSerializer

class AppartementTypeViewSet(viewsets.ModelViewSet):
    queryset = AppartementType.objects.all()
    serializer_class = AppartementTypeSerializer
