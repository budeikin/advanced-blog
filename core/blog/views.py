from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from blog.models import Post
from blog.forms import CreatePostForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class PostList(LoginRequiredMixin ,ListView):
    # queryset = Post.objects.all()
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 3
    
    def get_queryset(self):
        posts = Post.objects.filter(status=True).order_by('-id')
        return posts
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['time'] = timezone.now()
        return context


class PostCreateView(CreateView):
   model = Post
   form_class = CreatePostForm
   success_url = '/blog/list/'

   def form_valid(self, form):
       form.instance.author = self.request.user
       return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = CreatePostForm
    success_url = '/blog/list'


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')