from django.shortcuts import render
from django.views.decorators.http import require_http_methods


articles = [
    {'title': '"How to foo?"', 'author': 'F. BarBaz'},
    {'title': '"Force 101"', 'author': 'O-W. Kenobi'},
    {'title': '"Top 10 skyscrapers"', 'author': 'K. Kong'},
    {'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla'},
    {'title': '"5 min recepies"', 'author': 'H. Lector'},
]

# BEGIN (write your solution here)
@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        article = {
            'title': request.POST['title'],
            'author': request.POST['author']
        }
        articles.append(article)
    return render(request, 'articles.html', context={'articles': articles})