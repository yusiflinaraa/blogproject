from django.contrib import admin

from .models import Author, Category, Post
from .models import Tag

admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
