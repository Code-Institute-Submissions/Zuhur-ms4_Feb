from django.shortcuts import redirect, render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            subject = 'Inquiry'
            data = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'message': message,
            }
            message = '''
            {}
            From: {}
            '''.format(data['message'], data['email'])
            try:
                send_mail(subject, message, '', ['fitnessjogym@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    form = ContactForm()
    return render(request, 'gym_app/home.html', {'form': ContactForm()})
