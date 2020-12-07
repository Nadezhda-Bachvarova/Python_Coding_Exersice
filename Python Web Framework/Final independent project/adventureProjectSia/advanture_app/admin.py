from django.contrib import admin

from advanture_app.models import Like, Article, Comment


class LikeInLine(admin.TabularInline):
    model = Like


class ArticleAdmin(admin.ModelAdmin):
    fields = ('user', 'title', 'hashtag', 'destination', 'content')
    list_display = ('user', 'destination')
    list_filter = ('user', 'title', 'hashtag', 'destination')
    inlines = (
        LikeInLine,
    )


class CommentAdmin(admin.ModelAdmin):
    fields = ('user', 'article', 'text')
    list_display = ('user', 'article')
    list_filter = ('user',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)
