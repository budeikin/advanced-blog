from rest_framework.decorators import api_view,permission_classes, action
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from blog.api.v1.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status,mixins,viewsets
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer,CategorySerializer
from ...models import Post,Category
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import ResultSetPagination


# Class Base Views
'''class PostList(APIView):
    """ getting a list of post and creatind new posts""" 
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self,request):
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''
    
'''
class PostList(ListCreateAPIView):
    """ getting a list of post and creatind new posts"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)'''

  


'''
class PostDetail(APIView):
    """" getting detail of the object and edit plus removing it """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self,request,id):
        """ retriveing the post data """
        post = get_object_or_404(Post,pk=id)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self,request,id):
        """ editing the post data """
        post = get_object_or_404(Post,pk=id)
        serializer = self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,id):
        """ removing the post  """
        post = get_object_or_404(Post,pk=id)
        post.delete()
        return Response('removed successfully',status=status.HTTP_202_ACCEPTED)
        
'''

'''class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)'''

   

# Function Base Views
"""
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
    
"""
"""
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request,id):
    post = get_object_or_404(Post,pk=id)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response('removed successfully',status=status.HTTP_202_ACCEPTED)

"""

# Example of ViewSets Views

class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    pagination_class = ResultSetPagination
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields={'categoy':['exact','in'],'author':['exact']}
    search_fields = ['title']
    ordering_fields=['publishes_date']

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()