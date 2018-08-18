from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')

def count(request) :
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    lettercounting = list(map(len, fulltext.split()))
    worddic = {}
    for word in wordlist :
        if word in worddic :
            worddic[word] += 1
        else :
            worddic[word] = 1
    sortedwords = sorted(worddic.items(), key=operator.itemgetter(1), reverse = True)
    return render(request, 'count.html',{"fulltext":fulltext, 'count':len(wordlist), 'sortedwords': sortedwords, 'lettercounting':lettercounting})

def about(request) :
    return render(request, 'about.html')
