from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from ask.qa.models import Question, Answer
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404

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
    return page

def new_questions(request):
    questions = Question.objects.new()
    page = paginate(request, questions)
    return render(request, 'qa/new_questions.html', {
        'questions': page.object_list,
        'page': page,
    })

def popular_questions(request):
    questions = Question.objects.popular()
    page = paginate(request, questions)
    return render(request, 'qa/popular_questions.html', {
        'questions': page.object_list,
        'page': page,
    })

def question_details(request):
    question = get_object_or_404(Question)
    answers = Answer.objects.filter(question=question)
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers,
    })

