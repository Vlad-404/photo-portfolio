from django.shortcuts import render
from .models import categories

# Create your views here.
def index(request):
    category = categories.objects.all()
    context = {
        'category': category
    }
    # base index.html view
    return render(request, 'home/index.html', context)
