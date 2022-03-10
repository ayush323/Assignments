from django.contrib import admin
from .models import Author, post, Tag, comments

admin.site.register(Author)
admin.site.register(post)
admin.site.register(Tag)
admin.site.register(comments)