from django.shortcuts import render
from questions import models, views, forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

class CreateQuestion(LoginRequiredMixin,generic.CreateView):

    template_name = 'questions/question_form.html'
    form_class = forms.QuestionForm
    success_url = reverse_lazy('home')
    model = models.Question

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


@login_required
def answer(request):
    if request.method == 'POST':
        form = forms.AnswerForm(request.POST)

        if form.is_valid():
            user = request.user
            answer = models.Answer()
            answer.user = request.user
            answer.question = form.cleaned_data.get('question')
            answer.description = form.cleaned_data.get('description')
            answer.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')

def question(request,pk):
    question = get_object_or_404(models.Question, pk=pk)
    form = forms.AnswerForm(initial={'question':question})
    return render(request,'questions/question.html', {
        'question':question,
        'form': form
})
