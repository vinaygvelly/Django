from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

TEMPLATES_DIRS= (
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    return render(request, "index.html")

def second(request):
    return render(request, "second.html")