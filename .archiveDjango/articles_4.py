# Форма поиска
<form class="form-inline mb-3" action="{% url 'articles_index' %}" method="get">
<div class="form-group">
    <input class="form-control" type="search" name="q" value="{{query }}" placeholder="Название статьи">
</div>
<button class="btn btn-info" type="submit">Поиск</button>
</form>
# Работа с поиском
class IndexView(View):
    # BEGIN (write your solution here)
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        articles = Article.objects.filter(Q(title__icontains=query))
        return render(
            request,
            'articles/index.html',
            context={
                'articles': articles,
                'query': query,
                }
            )