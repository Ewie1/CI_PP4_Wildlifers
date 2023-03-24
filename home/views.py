# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
import os
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
        your_name = request.POST['your-name']
        your_email = request.POST['your-email']
        your_message = request.POST['your-message']

        send_mail(
            'Message from' + your_name,
            your_message,
            your_email,  
            [os.environ.get('EMAIL_HOST_USER')]
             )
        messages.success(request, 'You message have been sent')

        return render(request, 'home/contact.html', {'your_name': your_name})
    else:
        return render(request, 'home/contact.html', {})
