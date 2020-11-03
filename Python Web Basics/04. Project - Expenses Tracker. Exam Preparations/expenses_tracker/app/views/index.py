from django.shortcuts import render

from app.common.budget import calculate_budget_left
from app.forms.profiles import ProfileForm
from app.models import Profile, Expense
from app.views.profile import create_profile


def index(request):
    if Profile.objects.exists():
        profile = Profile.objects.all()[0]
        expenses = Expense.objects.all()
        profile.budget_left = calculate_budget_left(profile, expenses)
        context = {
            'profile': profile,            #because the profile is one
            'expenses': expenses,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        return create_profile(request)

