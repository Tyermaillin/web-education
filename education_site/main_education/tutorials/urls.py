from django.urls import path
from . import views

app_name = 'tutorials'

urlpatterns = [
    path('', views.html_part_01, name='html_part_01'),
    path('bootstrap/basic_typography', views.basic_typography, name="basic_typography"),
    path('bootstrap/text_alignment_display', views.text_alignment_display, name="text_alignment_display"),
    path('bootstrap/floats_position', views.floats_position, name='floats_position'),
    path('bootstrap/colors_background', views.colors_background, name='colors_background'),
    path('bootstrap/spacing', views.spacing, name='spacing'),
    path('bootstrap/sizing', views.sizing, name='sizing'),
    path('bootstrap/breakpoints', views.breakpoints, name='breakpoints'),
    path('bootstrap/buttons', views.buttons, name='buttons'),
    path('bootstrap/navbar', views.navbar, name='navbar'),
    path('bootstrap/list_group_badges', views.list_group_badges, name='list_group_badges'),
    path('bootstrap/forms', views.forms, name='forms'),
    path('bootstrap/input_groups', views.input_groups, name='input_groups'),
    path('bootstrap/alerts_progress', views.alerts_progress, name='alerts_progress'),
    path('bootstrap/tables_pagination', views.tables_pagination, name='tables_pagination'),
    path('bootstrap/cards', views.cards, name='cards'),
    path('bootstrap/media_objects', views.media_objects, name='media_objects'),
]
