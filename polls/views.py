from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from polls.models import Question


def index(request):
    last_questions_list = Question.objects.order_by('pub_date')[:5]
    output = ','.join([q.question_text for q in last_questions_list])
    context = {
        'result': output
    }
    return render(request, '../templates/index.html', context)


def detail(request, question_id):
    response = ("Estas viendo la pregunta %s." % question_id)
    return HttpResponse(response)


def result(request, question_id):
    response = ("Resultado la pregunta %s." % question_id)
    return HttpResponse(response)


def vote(request, question_id):
    response = ("Resultado la pregunta %s." % question_id)
    return HttpResponse(response)
