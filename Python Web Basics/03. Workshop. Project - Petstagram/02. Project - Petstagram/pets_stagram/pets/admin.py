from django.contrib import admin

from pets.models import Pet, Like, Comment


class LikeInLine (admin.TabularInline):
    model = Like


class PetAdmin(admin.ModelAdmin):
    #fields = ('type', 'name', 'age') -> fields which show for fill in admin part
    list_display = ('type', 'name', 'age')      # grid in display in admin part
    list_filter = ('type', 'age')
    inlines = (
        LikeInLine,
    )


admin.site.register(Pet, PetAdmin)
admin.site.register(Comment)
admin.site.register(Like)