from django.contrib import admin

# Register your models here.
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'text']
    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)
