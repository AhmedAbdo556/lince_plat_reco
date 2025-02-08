from rest_framework import serializers
from .models import File,User,Person


class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = ('file', 'remark', 'timestamp')




class userSerializer(serializers.ModelSerializer):
    class Metaa():

        model = User
        fields =('first_name' , 'last_name' , 'email' , 'password')




   

