from django.db import models

class SessionConfiguration(models.Model):
    screen_size = models.CharField(max_length=10)
    cell_size = models.IntegerField()
    ruleset_name = models.CharField(max_length=50)
    aging = models.BooleanField()
    processing_mode = models.IntegerField(choices=[(1, 'CPU'), (2, 'GPU')])
    show_colors = models.BooleanField()
    seed_image_path = models.FilePathField(path='D:\chaos\extra')
