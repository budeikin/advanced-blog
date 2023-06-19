from django.urls import path
from blog.api.v1 import views
from rest_framework import routers

app_name = 'api-v1'

router = routers.DefaultRouter()
router.register('post',views.PostModelViewSet,basename='post')
router.register('category',views.CategoryModelViewSet,basename='category')

urlpatterns = router.urls

'''
urlpatterns =[
    # path('post/',post_list,name='post-list'),
    # path('post/<int:id>/',post_detail,name='post-detail'),
    # path('post/',PostList.as_view(),name='post-list'),
    # path('post/<int:pk>/',PostDetail.as_view(),name='post-detail'),
    path('post/',views.PostViewSet.as_view({'get':'list','post':'create'}),name='post-list'),
    path('post/<int:pk>/',views.PostViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update',
                                                     'delete':'destroy'}),name='post-list'),

]
'''