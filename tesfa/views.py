from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    published = Post.objects.filter(status = 1)
    return render(request, 'tesfa/post/list.html', {'published' : published})
def post_detail(request, param1, param2):
    current_post = Post.objects.get(id=param2)
    return render(request, 'tesfa/post/detail.html', {'post' : current_post})
