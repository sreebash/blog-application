from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView

from blog.forms import CommentForm, PostCreateForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    fields = ['title', 'description', 'feature_image', 'author']


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("blog:post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# class PostDetailView(DetailView):
#     model = Post


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    new_comment = None

    comments = post.comment.all()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        new_comment = comment_form.save(commit=False)
        new_comment.post = post
        new_comment.save()

    comment_form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'new_comment': new_comment
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    print(post)
    if request.user == post.author:
        post.delete()
        messages.warning(request, 'Post deleted successfully.')
        return redirect('blog:post_list')

    return redirect('blog:post_list')
