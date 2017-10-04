from django.shortcuts import render
from posts import models
from posts import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.core.urlresolvers import reverse_lazy




# Create your views here.

class CreatePost(LoginRequiredMixin,generic.CreateView):

    template_name = 'posts/post_form.html'
    form_class = forms.PostForm
    success_url = reverse_lazy('home')
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
