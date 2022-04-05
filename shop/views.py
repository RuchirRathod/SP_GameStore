from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from shop.models import Game
# Create your views here.
def index(request):
    if request.method == "GET":
        return HttpResponse("Hello World!")

def get_games(request):
    if request.method == "GET":
        game = Game.objects.all()[0]
        return HttpResponse(str(game.title) + " Rs " + str(game.price))
        
def get_html(request):
    games = ["Pacman", "GTA", "Hitman"]
    if request.method == "GET":
        return render(request,'shop/login.html', {"games":games})