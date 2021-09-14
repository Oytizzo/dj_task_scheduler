from django import forms

from .tasks import send_email_task


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))
    sender = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    cc_myself = forms.BooleanField(required=False)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        send_email_task.delay(self.cleaned_data['subject'],
                              self.cleaned_data['message'],
                              self.cleaned_data['sender'],
                              self.cleaned_data['cc_myself'])
