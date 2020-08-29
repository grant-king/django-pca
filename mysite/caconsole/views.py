from django.shortcuts import render
from django.http import HttpResponse
from .models import SessionConfiguration
import pythoncellularautomata.models.session_models as pca


def index(request):
    return HttpResponse("You're at the cellular automata console index.")

def play_default(request):
    session_manager = pca.SessionConfigurationManager()
    session_manager.play_default()
    return HttpResponse("This page plays the default automaton.")

def all_configurations(request):
    all_configurations = SessionConfiguration.objects.all()
    html_configs = '<br>'.join([config.name for config in all_configurations])
    return HttpResponse(f'All configs:<br>{html_configs}')

