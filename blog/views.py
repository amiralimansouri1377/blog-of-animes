from django.urls import reverse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from .models import Post, Comment
from .form import CommentForm

from .models import Post, Comment

# Create your views here.
class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-pub_date"]

    def get_queryset(self):

        qeuryset = super().get_queryset()
        data = qeuryset[:3]
        return data
    

# class AllPostsView(ListView):
#     template_name = "blog/index.html"
#     model = Post
#     context_object_name = "posts"

def all_post(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page", 1)
    posts = paginator.page(page_number)

    return render(request, "blog/all-post.html", {
        "posts": posts,
        "page_range": paginator.page_range
    })


class DetailPostView(DetailView):
    template_name = "blog/detail-post.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        context["form"] = form
        return context


class AddCommentView(CreateView):
    template_name = "blog/comment-form.html"
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post_id = self.kwargs.get("pk")
        post = Post.objects.get(pk=post_id)
        comment = form.save(commit=False)
        self.success_url = reverse("detail-post", args=[post.slug])
        comment.post = post
        comment.save()
        return super().form_valid(form)
