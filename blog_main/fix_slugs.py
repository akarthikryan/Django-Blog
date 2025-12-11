from django.core.management.base import BaseCommand
from blogs.models import Blog
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Fix missing slugs for Blog posts'

    def handle(self, *args, **options):
        for post in Blog.objects.all():
            if not post.slug:
                base_slug = slugify(post.title)
                slug = base_slug
                counter = 1
                while Blog.objects.filter(slug=slug).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                post.slug = slug
                post.save()
                self.stdout.write(self.style.SUCCESS(f"Fixed slug for: {post.title} → {post.slug}"))
