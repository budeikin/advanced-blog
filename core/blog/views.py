from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from accounts.models import Profile
from blog.models import Post
from django.http import HttpResponse
from blog.forms import CreatePostForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'blog/index.html'


class PostList(LoginRequiredMixin, ListView):
    # queryset = Post.objects.all()
    template_name = "blog/list.html"
    context_object_name = "posts"
    login_url = 'http://127.0.0.1:8000/account/login/'
    paginate_by = 3

    def get_queryset(self):
        posts = Post.objects.filter(status=True).order_by("-id")
        return posts


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "blog/detail.html"
    login_url = 'http://127.0.0.1:8000/account/login/'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["time"] = timezone.now()
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = CreatePostForm
    success_url = "/blog/list/"

    def form_valid(self, form):
        profile=Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = CreatePostForm
    success_url = "/blog/list"


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post-list")
