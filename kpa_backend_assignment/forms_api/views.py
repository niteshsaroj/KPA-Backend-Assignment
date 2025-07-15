from rest_framework import viewsets
from .models import *
from .serializers import *

class BogieChecksheetFormViewSet(viewsets.ModelViewSet):
    queryset = BogieChecksheetForm.objects.all()
    serializer_class = BogieChecksheetFormSerializer
    http_method_names = ['post']  # Allow only POST

class WheelSpecificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WheelSpecification.objects.all()
    serializer_class = WheelSpecificationSerializer
