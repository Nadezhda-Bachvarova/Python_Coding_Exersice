from django.urls import path

from advanture_app import views
from advanture_app.views import article_details_or_comment, unauthorised_message, article_List, \
    delete_article, like_article, edit_article

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('details/<int:pk>/', article_details_or_comment, name='article details or comment'),
    path('creat/', views.ArticleCreateView.as_view(), name='article creat'),
    path('edit/<int:pk>', edit_article, name='edit article'),
    # path('edit/<int:pk>', views.ArticleUpdateView.as_view(), name='article edit'),
    path('delete/<int:pk>', delete_article, name='delete article'),
    path('like/<int:pk>/', like_article, name='like article'),
    path('unknown/', unauthorised_message, name='message'),
    path('list/', article_List, name='articles'),
]