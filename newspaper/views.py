from django.views.generic import ListView
from .models import Article

#Creatre your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    
    