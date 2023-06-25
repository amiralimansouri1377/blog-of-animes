from django.contrib import admin
from .models import Post, Tag, Author

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author")
    list_filter = ("author", "tag")

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)