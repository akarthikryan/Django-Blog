from django.shortcuts import render, get_object_or_404, redirect
from blogs.models import Blog, Category, Comment
from django.db.models import Q
from django.http import HttpResponseRedirect

# -------------------- Category-wise Posts --------------------
def posts_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    blogs = Blog.objects.filter(status='Published', category=category)

    # Optional: latest featured post
    featured_post = Blog.objects.filter(status='Published').order_by('-created_at').first()

    context = {
        'blogs': blogs,
        'category': category,
        'featured_post': featured_post,
    }
    return render(request, 'posts_by_category.html', context)


# -------------------- Single Blog View --------------------
def blogs(request, slug):
    # Get the post by slug (model guarantees uniqueness)
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    
    # Comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    
    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
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
