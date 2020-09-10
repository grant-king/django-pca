from django.shortcuts import render
from django.http import HttpResponse
from .models import SessionConfiguration
import pythoncellularautomata.models.session_models as pca

def index(request):
    return render(request, 'caconsole/index.html')

def play_default(request):
    session_manager = pca.SessionConfigurationManager()
    session_manager.play_default()
    return HttpResponse("This page plays the default automaton.")

def all_configurations(request):
    context = {
        'all_configurations': SessionConfiguration.objects.all()
    }
    return render(request, 'caconsole/all_configs.html', context)

def configuration_detail(request, configuration_id):
    context = {
        'configuration': SessionConfiguration.objects.get(pk=configuration_id)
    }
    return render(request, 'caconsole/config_detail.html', context)

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
    return HttpResponse(f'{configuration.name} simulation has been stopped.')



