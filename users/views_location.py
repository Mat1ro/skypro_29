from rest_framework.viewsets import ModelViewSet

from users.models import Location
from users.serializers_location import LocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
