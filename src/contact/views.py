from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import FormView

from .forms import ContactForm
from .tasks import add, send_mail_task


def index(request):
    add.delay(5, 6)
    return HttpResponse("<h1>Hello, world</h1>")


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact/contact_form.html'
    form_class = ContactForm
    success_url = '/blog/'
    success_message = "You've sent an email to contact. Thank you!"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


def contact_view(request):
    send_mail_task.delay()
    context = {}
    return render(request, 'contact/contact.html', context)


def dev_contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            message_to_email = message + f"\n\nEmailed From: {sender}"

            recipients = ['oytizzo@gmail.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message_to_email, sender, recipients)

            messages.success(request,
                             f'Thanks for your consideration. I will get in touch with you as soon as possible!')
            return redirect('index')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact_form.html', context)
