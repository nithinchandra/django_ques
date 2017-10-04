from django import forms
from questions import models

class QuestionForm(forms.ModelForm):
    title = forms.CharField(required=True)
    description = forms.Textarea()


    class Meta:
        model = models.Question
        fields = ['title','description','tags']

class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                        queryset=models.Question.objects.all())

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control', 'rows':'4'}),
        max_length=2000)

    class Meta:
        model = models.Answer
        fields = ['question','description']
