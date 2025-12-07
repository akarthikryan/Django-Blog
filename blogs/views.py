from django.shortcuts import render, get_object_or_404
from blogs.models import Blog, Category


def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = get_object_or_404(Category, pk=category_id)

    featured_post = Blog.objects.filter(status='Published').order_by('-created_at')[:1]

    context = {
        'posts': posts,
        'category': category,
        'featured_post': featured_post,
        
    }

    return render(request, 'posts_by_category.html', context)
