from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Article
from django.urls import reverse_lazy

#Creatre your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'article_list'
    
class ArticleDetailView(DetailView):
        model = Article
        template_name = 'article-detail.html'
        context_object_name = 'article'
        
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article-create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article-update.html'
    fields = ['title', 'content']

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)
    
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article-delete.html'
    success_url = reverse_lazy('article-list')

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)
    