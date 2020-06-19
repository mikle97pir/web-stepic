from django import forms
from .models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea, max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    def clean(self):
        pass
    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
    def __init__(self, question, *args, **kwargs):
        self.question = question
        super(AnswerForm, self).__init__(*args, **kwargs)
    def clean(self):
        pass
    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
