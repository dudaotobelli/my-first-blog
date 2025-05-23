from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request): 
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
form = PostForm()
return render(request, 'blog/post_edit.html', {'form': form})

if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
     post = form.save(commit=False)
     post.author = request.user
     post.published_date = timezone.now()
     post.save()
else:
    form = PostForm()

from django.shortcuts import render, get_object_or_404
