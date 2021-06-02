from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import auth, User


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


def login(request):


    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['id']='1'
            messages.info(request, "Log-in Successful...")
            return redirect('/index')
        else:
            messages.info(request, " User not found")
            return redirect('/login')
    else:
        if request.session.get('id') == '1':
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':

        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, '* Username taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, '* email taken')
                return redirect('/signup')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
                user.save();
                messages.info(request, '* Signup Successful... Please Login...')
                return redirect('/login')
        else:
            messages.info(request, '* Password is not match')
            return redirect('/signup')
    else:
        return render(request, 'signup.html')



def logout(request):
    auth.logout(request)
    return redirect('/login')