from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from .forms import QuoteForm, AuthorForm, TagForm

from .models import Quote, Tag, Author
# Create your views here.
from .utils import get_mongodb


def main(request, page=1):
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, 10)
    page_obj = paginator.get_page(page)
    tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]
    context = {'quotes': page_obj, 'tags': tags}
    return render(request, 'quotes/index.html', context)



def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to="quotes:root")
        else:
            return render(request, "quotes/add_quote.html", context={'form': QuoteForm(), "message": "Form is not valid"})
    return render(request, "quotes/add_quote.html", context={'form': QuoteForm()})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save()
            return redirect(to="quotes:root")
        else:
            return render(request, "quotes/add_author.html", context={'form': AuthorForm(), "message": "Form is not valid"})
    return render(request, "quotes/add_author.html", context={'form': AuthorForm()})


def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            tag = Tag(name=name)
            tag.save()
            return redirect('quotes:root')
    else:
        form = TagForm()
    return render(request, 'quotes/add_tag.html', {'form': form})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'quotes/author_detail.html', {'author': author, 'quotes': quotes})


def tag_quotes(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    quotes = Quote.objects.filter(tags__name=tag_name)

    context = {
        'tag': tag,
        'quotes': quotes,
    }
    return render(request, 'quotes/tag_quotes.html', context)



