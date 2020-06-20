from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UsernameField
from .models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea, max_length=191)
    text = forms.CharField(widget=forms.Textarea)
    def clean(self):
        pass
    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question
    def __init__(self, *args, user=None, **kwargs):
        self._user = user
        super(AskForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Заголовок вопроса:'
        self.fields['text'].label = 'Текст вопроса:'


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(
        queryset=Question.objects.all(),
        widget = forms.HiddenInput,
    )
    def __init__(self, *args, user=None, **kwargs):
        self._user = user
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = 'Новый ответ:'
        self.fields['question'].label = ''
    def clean(self):
        pass
    def save(self):
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignUpForm(forms.ModelForm):
    username = UsernameField()
    email = forms.EmailField(max_length=191)
    password = forms.CharField(
        label= "Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
    def clean(self):
        pass
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
