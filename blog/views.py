from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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
    