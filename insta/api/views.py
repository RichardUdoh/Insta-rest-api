from django.shortcuts import render, redirect , get_object_or_404, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import LikeSerializer, CommentSerializer, PostSerializer
from .models import Post, Like, Comment
from .forms import PostForm, CommentForm
from django.views.generic import (
    ListView,
    CreateView,
)
# Create your views here.

class PostListView(ListView):
    template_name = "api/post_list.html"
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3

class PostCreateView(CreateView):
    template_name = "api/post_create.html"
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user 
        return super().form_valid(form)

# class PostCommentView(CommentView):
#     template_name = "api/post_list.html"
#     form_class = CommentForm
#     queryset = Post.objects.all()
#     success_url = '/'

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         form.instance.user = self.request.user 
#         return super().form_valid(form)

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
    
# def comment_post(request):
#     user = request.user
#     post = 
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post 
#             comment.user = user
#             comment.save()
#             return redirect('api:post_list')


# def comment_post(request, post):

#     post = get_object_or_404(Post, slug=post)

#     comments = post.comments.filter(status=True)

#     user_comment = None

#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             user_comment = comment_form.save(commit=False)
#             user_comment.post = post
#             user_comment.save()
#             return HttpResponseRedirect('/' + post.slug)
#     else:
#         comment_form = CommentForm()
#     return render(request, 'single.html', {'post': post, 'comments':  user_comment, 'comments': comments, 'comment_form': comment_form})


class Likelist(APIView):
    def get(self, request):
        like1 = Like.objects.all()
        serializer = LikeSerializer(like1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class Commentlist(APIView):
    def get(self, request):
        comment1 = Comment.objects.all()
        serializer = LikeSerializer(comment1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class Postlist(APIView):
    def get(self, request):
        post1 = Post.objects.all()
        serializer = PostSerializer(post1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
