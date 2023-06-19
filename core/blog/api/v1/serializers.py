from rest_framework import serializers
from ...models import Post,Category
from accounts.models import Profile


# class PostSerialize(serializers.Serializer): 
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.CharField(source='get_absolute_api_url',read_only=True)
    # absolute_url = serializers.SerializerMethodField()
    # categoy = serializers.SlugRelatedField(
    #     many=False,
    #     slug_field='name',
    #     queryset=Category.objects.all()
    # )
    # categoy=CategorySerializer()
    
    class Meta:
        model = Post
        fields = ['id','images','author','title','content','snippet','categoy','status','relative_url','publishes_date']
        read_only_fields = ['author']

    # def get_absolute_url(self,obj):
    #     request = self.context.get('request')
    #     return request.build_absolute_url(obj.pk)

    def to_representation(self,instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet')
            rep.pop('relative_url')
        else:
            rep.pop('content')
        rep['categoy'] = CategorySerializer(instance.categoy,context={'request':request}).data
        
        # rep['categoy']  = CategorySerializer(instance.categoy).data
        return rep

    def create(self,validate_data):
        user_id = self.context.get('request').user.id
        validate_data['author'] = Profile.objects.get(user__id=user_id)
        return super().create(validate_data)
    

