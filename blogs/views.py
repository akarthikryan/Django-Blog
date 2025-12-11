from django.shortcuts import render, get_object_or_404
from blogs.models import Blog, Category
from django.db.models import Q

# -------------------- Category-wise Posts --------------------
def posts_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Blog.objects.filter(status='Published', category=category)

    # Optional: latest featured post
    featured_post = Blog.objects.filter(status='Published').order_by('-created_at').first()

    context = {
        'posts': posts,
        'category': category,
        'featured_post': featured_post,
    }
    return render(request, 'posts_by_category.html', context)


# -------------------- Single Blog View --------------------
def blogs(request, slug):
    # Get the post by slug (model guarantees uniqueness)
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')

    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blogs.html', context)


# -------------------- Search --------------------
def search(request):
    keyword = request.GET.get('keyword', '')

    blogs = Blog.objects.filter(
        Q(title__icontains=keyword) |
        Q(short_description__icontains=keyword) |
        Q(blog_body__icontains=keyword),
        status='Published'
    )

    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)
