import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split()

    wordDictionary = {}
    for word in wordList:
        wordDictionary[word] = wordDictionary.get(word, 0) + 1

    sortedwords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',
                  {'fulltext': fulltext, 'count': len(wordList), 'wordDictionary': sortedwords})
