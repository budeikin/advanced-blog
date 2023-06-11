from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import PostSerialize
from ...models import Post
# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerialize(posts,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerialize(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




# Function Base Views
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request,id):
    post = get_object_or_404(Post,pk=id)

    if request.method == 'GET':
        serializer = PostSerialize(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerialize(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response('removed successfully',status=status.HTTP_202_ACCEPTED)

