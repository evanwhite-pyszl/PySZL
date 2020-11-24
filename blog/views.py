from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Post


def overview(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))


def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post.html', {'post': post})
