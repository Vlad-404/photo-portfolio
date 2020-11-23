from django.shortcuts import render


# Create your views here.
def index(request):
    # base index.html view
    return render(request, 'home/index.html')
