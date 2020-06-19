from django import forms
from .models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea, max_length=191)
    text = forms.CharField(widget=forms.Textarea)
    def clean(self):
        pass
    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question
    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Заголовок вопроса:'
        self.fields['text'].label = 'Текст вопроса:'


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(
        queryset=Question.objects.all(),
        widget = forms.HiddenInput,
    )
    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = 'Новый ответ:'
        self.fields['question'].label = ''
    def clean(self):
        pass
    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer