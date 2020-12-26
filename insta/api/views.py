from django.shortcuts import render, redirect
from .models import Post, Like
from .forms import PostForm
from django.views.generic import (
    ListView,
    CreateView,
)
# Create your views here.

class PostListView(ListView):
    template_name = "api/post_list.html"
    queryset = Post.objects.all()
    context_object_name = 'posts'


class PostCreateView(CreateView):
    template_name = "api/post_create.html"
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user 
        return super().form_valid(form)


def like_post(request):
    # print('This method works HURRAY!!!!')
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return redirect('api:post_list')
    