from django.shortcuts import render
from django.http import HttpResponse
import pythoncellularautomata.models.session_models as pca


def index(request):
    session_manager = pca.SessionConfigurationManager()
    session_manager.play_default()
    return HttpResponse("You're at the cellular automata console index.")
