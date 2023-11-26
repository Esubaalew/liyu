from django.contrib import admin
from .models import Post
from .models import Category
from .models import Author
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ['title', 'slug', 'author', 'modified', 'published']
    search_fields = ('title', 'content')
    list_filter= ('author', 'published', 'publisher', )
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category)
admin.site.register(Author)