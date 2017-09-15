from rest_framework.serializers import ModelSerializer
from myauth.models import MyUser
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

class MyUserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'ra',
            'level',
        )

