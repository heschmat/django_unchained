from django.shortcuts import render, HttpResponse

import random

compliments = [
    "You have an amazing ability to bring out the best in others.",
    "Your smile is contagious.",
    "You light up the room just by being in it.",
    "Your creativity knows no bounds.",
    "You're a true friend, and I'm lucky to know you.",
    "Your positive energy is infectious.",
    "You have a heart of gold.",
    "Your laughter is the best sound in the world.",
    "You make the world a better place just by being in it.",
    "You're incredibly thoughtful and considerate."
]


# Create your views here.
def home(req):
    return HttpResponse("Hello World!")

def compliment(req, name):
    msg = random.choice(compliments)
    return HttpResponse(f'Bonjour {name.title()}. {msg}')

def gen_rnd_number(req, a, b):
    return HttpResponse(f'Your lucky number is {random.randint(a, b)}!')
