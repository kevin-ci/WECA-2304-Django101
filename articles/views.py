from django.shortcuts import render
from .models import Article


# Create your views here.
def view_article(request, id):
    retrieved_article = Article.objects.get(id=id)
    context = { "article": retrieved_article }
    return render(request, 'articles/index.html', context)