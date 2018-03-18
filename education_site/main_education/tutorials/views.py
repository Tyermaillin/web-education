from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tutorials/index.html')

def html_part_01(request):
    return render(request, 'tutorials/html_part_01.html')

def basic_typography(request):
    return render(request, 'tutorials/0.1_basic_typography.html')

def text_alignment_display(request):
    return render(request, 'tutorials/0.2_text_alignment_display.html')

def floats_position(request):
    return render(request, 'tutorials/0.3_floats_position.html')

def colors_background(request):
    return render(request, 'tutorials/0.4_colors_background.html')

def spacing(request):
    return render(request, 'tutorials/0.5_spacing.html')

def sizing(request):
    return render(request, 'tutorials/0.6_sizing.html')

def breakpoints(request):
    return render(request, 'tutorials/0.7_breakpoints.html')



def buttons(request):
    return render(request, 'tutorials/0.8_buttons.html')

def navbar(request):
    return render(request, 'tutorials/0.9_navbar.html')

def list_group_badges(request):
    return render(request, 'tutorials/1.0_list_group_badges.html')

def forms(request):
    return render(request, 'tutorials/1.1_forms.html')

def input_groups(request):
    return render(request, 'tutorials/1.2_input_groups.html')

def alerts_progress(request):
    return render(request, 'tutorials/1.3_alerts_progress.html')

def tables_pagination(request):
    return render(request, 'tutorials/1.4_tables_pagination.html')

def cards(request):
    return render(request, 'tutorials/1.5_cards.html')

def media_objects(request):
    return render(request, 'tutorials/1.6_media_objects.html')
