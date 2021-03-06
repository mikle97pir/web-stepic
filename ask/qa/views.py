from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Answer
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404

from .forms import AnswerForm, AskForm, SignUpForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def test(request, *args, **kwargs):
    return HttpResponse('OK\n')

def paginate(request, questions):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = request.GET.get('page', 1)
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator

def new_questions(request):
    questions = Question.objects.new()
    page, paginator = paginate(request, questions)
    base_url = ''.join((reverse('root'), '?page='))
    return render(request, 'qa/new_questions.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
        'base_url': base_url,
    })

def popular_questions(request):
    questions = Question.objects.popular()
    page, paginator = paginate(request, questions)
    base_url = ''.join((reverse('popular'), '?page='))
    return render(request, 'qa/popular_questions.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
        'base_url': base_url,
    })

def question_add(request):
    if request.method == 'POST':
        form = AskForm(request.POST, user=request.user)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {
        'form':form,
    })

def question_details(request, id):
    question = get_object_or_404(Question, id=id)
    answers = Answer.objects.filter(question_id=id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, initial={'question':question}, user=request.user)
        if form.is_valid():
            form.save()
        return render(request, 'qa/question.html', {
            'question': question,
            'answers': answers,
            'form': form
        })
    else:
        form = AnswerForm(initial={'question':question})
        return render(request, 'qa/question.html', {
            'question': question,
            'answers': answers,
            'form': form
        })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=my_password)
            login(request, user)
            return HttpResponseRedirect(reverse('root'))
        else:
            return render(request, 'qa/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'qa/signup.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=my_password)
            login(request, user)
            return HttpResponseRedirect(reverse('root'))
        else:
            return render(request, 'qa/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'qa/signin.html', {'form': form})