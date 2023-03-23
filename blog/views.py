from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from .models import Post
from .forms import CommentForm


class PostDisplay(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_date")
    template_name = 'blog/blog_list.html'
    paginate_by = 4


class ReadPost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_date")
        return render(
            request, 'blog/blog_story.html',
            {'post': post,
             'comments': comments,
             'comment_form': CommentForm()
             }
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_date")
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Comment pending approval')
        else:
            comment_form = CommentForm()
            messages.error(request, 'Try again')

        return render(request, 'blog/blog_story.html',
            {'post': post,
             'comments': comments,
             'commented': True,
             'comment_form': CommentForm()
             } )