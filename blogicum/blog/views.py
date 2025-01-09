from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Post, Category


def index(request):
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=now(),
        category__is_published=True
    ).order_by('-pub_date')[:5]

    return render(request,
                  'blog/index.html',
                  {'post_list': posts}
                  )


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        is_published=True,
        pub_date__lte=now(),
        category__is_published=True
    )
    return render(request,
                  'blog/detail.html',
                  {'post': post}
                  )


def category_posts(request, category_slug):
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True
                                 )
    posts = category.post_set.filter(
        is_published=True,
        pub_date__lte=now()
    ).order_by('-pub_date')

    return render(request,
                  'blog/category.html',
                  {'category': category, 'posts': posts}
                  )
