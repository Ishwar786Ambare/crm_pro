from django.contrib import admin

from blog.models import Post, Category, Author

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Author)
