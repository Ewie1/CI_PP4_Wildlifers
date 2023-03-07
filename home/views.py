from django.shortcuts import render

# Create your views here.


def home(request):
    """
    View to render home page
    """
    return render(request, 'home/index.html')


def contact(request):
    """
    Function to dispaly contact form
    """

    if request.method == 'POST':
        your_name = request.POST['your_name']
        your_email = request.POST['your_email']
        your_message = request.POST['tour_message']
        return render(request, 'home/contact.html', {})
    else:
        return render(request, 'home/contact.html', {})