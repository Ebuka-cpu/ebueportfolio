from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.core.mail import send_mail


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        return context


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        send_mail(
            'message from' + message_email,
            message,
            message_email,
            ['anyaegbuebukafelix@yahoo.com']

        )

        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html')
