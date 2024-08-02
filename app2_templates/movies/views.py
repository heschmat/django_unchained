from django.shortcuts import render

import random

best_movies = [
    'Creed I',
    'Se7en',
    'Destination Wedding',
    'Nightmare Alley',
    'Good Will Hunting',
    'The Intouchables',
    "We're the Millers",
    'The Big Sick'
]

# Create your views here.
def home(req):
    context = {'movie': random.choice(best_movies)}
    return render(req, 'movies/index.html', context= context)

def top_movies(req):
    context = {'movies': best_movies}
    return render(req, 'movies/favorites.html', context= context)