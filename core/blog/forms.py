from django.forms import ModelForm, Form
from blog.models import Post


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "status", "categoy", "publishes_date"]


class EditPostForm(Form):
    class Meta:
        model = Post
        fields = ["title", "content", "status", "categoy", "publishes_date"]
