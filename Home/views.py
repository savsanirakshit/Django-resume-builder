from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

def Home(request):
    return render(request, 'index.html')

def Resume(request):
    return render(request, 'resume.html')

def Portfolio(request):
    return render(request, 'blog-3-columns.html')

def Contact(request):
    return render(request, 'contact.html')

def Email(request):

    send_mail(
        request.POST['subject'],
        request.POST['message'],
        request.POST['email'],
        ['savsanirakshit@gmail.com'],
        fail_silently=True,
    )

    messages.info(request, '* Your Message Send Successfully. You Will Get Reply Within 24 hour.')
    return render(request, 'contact.html')