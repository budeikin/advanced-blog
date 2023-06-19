from django.urls import path,include
from blog import views


app_name= 'blog'

urlpatterns = [
    # path('fbv-index',views.IndexView,name='fbv-index'),
    # path('cbv-index',views.IndexView.as_view(),name='cbv-index'),
    path('list/',views.PostList.as_view(),name='post-list'),
    path('detail/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('post/create/',views.PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/edit/',views.PostEditView.as_view(),name='post-edit'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post-delete'),
    path('api/v1/',include('blog.api.v1.urls'))
    # path('go_to_resume/<int:pk>',views.RedirectToResume.as_view(),name='redirect-to-resume')
]