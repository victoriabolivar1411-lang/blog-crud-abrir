from django.views.generic import (
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,    
)     
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
        
class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article-create.html'
    fields = ['title', 'author', 'content']
        
class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article-update.html'
    fields = ['title', 'content']
    
    