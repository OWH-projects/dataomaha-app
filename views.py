from models import *
from django.shortcuts import *
from django.db.models import *
#from your_project_name.models import *
from django.http import HttpResponse

def Main(request):
    dictionaries = {}
    return render_to_response('main.html', dictionaries)