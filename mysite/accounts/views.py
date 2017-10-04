from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy


from accounts import forms
# Create your views here.

class Signup(generic.CreateView):
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
