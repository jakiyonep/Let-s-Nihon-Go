from django.urls import path

from blog.views import IndexView, PostDetailView, CategoryListView, TagListView

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]