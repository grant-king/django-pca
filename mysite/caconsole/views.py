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

def configuration_detail(request, configuration_id):
    configuration = SessionConfiguration.objects.get(pk=configuration_id)
    config_attributes = [
        configuration.name,
        configuration.ruleset_name,
        configuration.seed_image_path,
    ]
    html_configuration = '<br>'.join(config_attributes)
    return HttpResponse(f'Config Details:<br>{html_configuration}')

def play_configuration(request, configuration_id):
    configuration = SessionConfiguration.objects.get(pk=configuration_id)
    pca_configuration = pca.SessionConfiguration(
        list(map(int, configuration.screen_size.split(','))),
        configuration.cell_size,
        configuration.ruleset_name,
        configuration.aging,
        configuration.processing_mode,
        configuration.show_colors,
        configuration.seed_image_path
    )
    sim = pca.CellularAutomatonSession(pca_configuration)
    return HttpResponse(f'That was configuration: {configuration_id}')



