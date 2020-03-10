from rest_framework import serializers
from django.contrib.auth.models import User, Group
from clasificador.models import Clasificar

#from datetime import datetime

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ClasificadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clasificar
        fields = ['fileid', 'fileName', 'fileUpload', 'dateC', 'dateU']