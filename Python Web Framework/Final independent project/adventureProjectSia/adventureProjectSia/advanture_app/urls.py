from django.urls import path

from adventureProjectSia.advanture_app import views
from adventureProjectSia.advanture_app.views import article_details_or_comment, unauthorised_message, article_list, \
    delete_article, like_article, edit_article, article_create

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('details/<int:pk>/', article_details_or_comment, name='article details or comment'),
    path('creat/', article_create, name='article creat'),
    path('edit/<int:pk>', edit_article, name='edit article'),
    # path('edit/<int:pk>', views.ArticleUpdateView.as_view(), name='article edit'),
    path('delete/<int:pk>', delete_article, name='delete article'),
    path('like/<int:pk>/', like_article, name='like article'),
    path('unknown/', unauthorised_message, name='message'),
    path('list/', article_list, name='articles'),
]
