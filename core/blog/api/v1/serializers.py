from rest_framework import serializers
from ...models import Post



# class PostSerialize(serializers.Serializer): 
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
    



class PostSerialize(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    