

from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path ("articulos/<int:pk>/", ArticleDetailView.as_view(), name='article-detail'),
    path('articulos/nuevo/', ArticleCreateView.as_view(), name='article-create'),
    path('articulos/<int:pk>/editar/', ArticleUpdateView.as_view(), name='article-update'),
    path('articulos/<int:pk>/eliminar/', ArticleDeleteView.as_view(), name='article-delete'),
    
    
    ]       