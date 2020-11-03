from django.contrib import admin

from app.models import Profile, Expense


class ProfileAdmin(admin.ModelAdmin):
    model = Profile


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Expense)