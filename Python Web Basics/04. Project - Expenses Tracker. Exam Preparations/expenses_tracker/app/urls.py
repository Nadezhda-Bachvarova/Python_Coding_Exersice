'''
    http://localhost:8000/ - home page
    • http://localhost:8000/create - create expense page
    • http://localhost:8000/edit/:id - edit expense page
    • http://localhost:8000/delete/:id - delete expense page
    • http://localhost:8000/profile - profile page
    • http://localhost:8000/profile/edit - profile edit page
    • http://localhost:8000/profile/delete - delete profile page
'''

from django.urls import path

from app.views.expenses import create_expense_page, edit_expense_page, delete_expense_page
from app.views.profile import profile_page, profile_edit_page, delete_profile_page, create_profile
from app.views.index import index

urlpatterns = [
    # Index = Home page
    path('', index, name='home page'),
    # Expenses
    path('create/', create_expense_page, name='create expense'),
    path('edit/<int:pk>/', edit_expense_page, name='edit expense'),
    path('delete/<int:pk>/', delete_expense_page, name='delete expense'),
    # Profile page
    path('profile/', profile_page, name='profile page'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', profile_edit_page, name='edit profile'),
    path('profile/delete/', delete_profile_page, name='delete profile'),
]
