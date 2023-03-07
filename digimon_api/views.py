from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import *
from .serializers import *

import json

class DigimonListView(ListCreateAPIView):

   
    serializer_class=DigimonListSerializer

    def get_queryset(self):
        user_email=self.request.query_params.get('email')
        return Digimon.objects.filter(email=user_email)


class DigimonDetailView(RetrieveUpdateDestroyAPIView):
   
    queryset = Digimon.objects.all()
    serializer_class = DigimonListSerializer