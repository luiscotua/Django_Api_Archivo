from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer, ClasificadorSerializer
from clasificador.models import Clasificar

from rest_framework.permissions import IsAuthenticated  # <-- Here

from rest_framework import generics
from rest_framework.response import Response
import csv
from django.conf import settings
import json

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class ClasificadorViewSet(viewsets.ModelViewSet):
    
    queryset = Clasificar.objects.all()
    serializer_class = ClasificadorSerializer
    permission_classes = [IsAuthenticated]

class clasificadorData(generics.RetrieveAPIView):
    queryset = Clasificar.objects.all()
    serializer_class = ClasificadorSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk):
        clasificador = Clasificar.objects.get(pk=pk)
        serielizador = ClasificadorSerializer(clasificador)

        data = []
        #leer
        with open('{}/{}'.format(str(settings.MEDIA_ROOT),str(clasificador.fileUpload))) as File:
            reader = csv.DictReader(File,  delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
            
            for row in reader:
                data.append(row)
        
        #filter
        if 'filtrar' in request.query_params:
            filtrar = request.query_params.get('filtrar') 
            data = json.dumps(data)
            data = json.loads(data)
            data = [(x) for x in data for l in x.values() if l.lower() == filtrar.lower()]
        
        #order
        if 'ordenar' in request.query_params:
            ordenar = request.query_params.get('ordenar')
            data = sorted(data, key=lambda i: i[ordenar].lower())
        if 'ordenar' in request.query_params and 'des' in request.query_params:
            ordenar = request.query_params.get('ordenar')
            des = request.query_params.get('des')
            if des.lower() == 'true':
                ordenar_reverse = True
            else:
                ordenar_reverse = False
            data = sorted(data, key=lambda i: i[ordenar].lower(), reverse = ordenar_reverse)
        
        return Response(data, status=200)





