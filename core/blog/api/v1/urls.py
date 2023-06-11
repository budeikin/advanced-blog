from django.urls import path
from blog.api.v1.views import post_detail,post_list

urlpatterns =[
    path('post/',post_list,name='post-list'),
    # path('post/',PostList.as_view(),name='post-list'),
    path('post/<int:id>/',post_detail,name='post-detail'),

]