from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index3(request):
    name = request.POST.get('name')
    lastname = request.POST.get('lastname')
    comment = request.POST.get('comment')
    vowel = 'aeiou'
    consonant = 'bcdfghjklmnpqrstvwxyz'
    count_vowel = 0
    count_consonant = 0
    for letter in comment:
        if letter in vowel:
            count_vowel += 1
        elif letter in consonant:
            count_consonant += 1
    return HttpResponse(f'Hello, {name} {lastname} \n Length your comment ={len(comment)}, Number of Vowels ={count_vowel}, Number of Consonants ={count_consonant}')