from django.views.generic import ListView, DetailView
from .models import Article

#Creatre your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'article_list'
    
class ArticleDetailView(DetailView):
        model = Article
        template_name = 'article-detail.html'
        context_object_name = 'article'
        
        