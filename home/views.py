from django.shortcuts import render

# Create your views here.


def home(request):
    """
    View to render home page
    """
    return render(request, 'index.html')
