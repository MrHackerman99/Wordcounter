from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, "home.html", {"hi_there":"This is me"})

def eggs(request):
    return HttpResponse("Fried")

def count(request):
    fulltext = request.GET["fulltext"]

    wordlist = fulltext.split()

    worddic = {}

    for word in wordlist:
        if word in worddic:
            #incraes
            worddic[word] += 1
        else:
            #add to dic
            worddic[word] = 1

    sortedWords = sorted(worddic.items(), key=operator.itemgetter(1), reverse=True)
    
    return render(request, "count.html", {"fulltext":fulltext, "count":len(wordlist), "sortedwords":sortedWords})

def about(request):
    return render(request, "about.html")