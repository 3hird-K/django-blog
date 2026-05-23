from django.shortcuts import render
from rest_framework import generics, status
from .models import Post
from rest_framework.response import Response
from .serializers import PostSerializer

# Create your views here.


def home(request):
    featured_posts = Post.objects.order_by('-created_at')[:6]
    total_posts = Post.objects.count()
    latest_post = Post.objects.order_by('-created_at').first()

    return render(
        request,
        'api/home.html',
        {
            'featured_posts': featured_posts,
            'total_posts': total_posts,
            'latest_post': latest_post,
        },
    )

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def delete(self, request, *args, **kwargs):
        Post.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'