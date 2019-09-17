from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, "home.html")

def aboutpage(request):
    return render(request, "about.html")

def count(request):
    fulltext = request.GET["fulltext"]
    words_count = fulltext.split()
    # fulltext_count = count(str(fulltext))

    fulltextlen = len(fulltext)

    return render(request, "count.html", {"fulltextkey": fulltext, "lenkey": fulltextlen, "wordcountkey": len(words_count)})
