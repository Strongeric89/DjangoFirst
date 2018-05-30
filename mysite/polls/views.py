from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Question, Choice
from django.template import loader, Template, RequestContext
from django.template.loader import render_to_string

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()
def index(request):

    latestQuestions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latestQuestions': latestQuestions}
    return render(request, 'polls/index.html',context)


def result(request, question_id):
    print('in result')
    return HttpResponse('result is %s' % question_id)


def detail(request, question_id):
    question = Question.objects.get(pk = question_id)
    return render(request, 'polls/detail.html', {'question':question})


def get_data(request):
    data = {
        "sales": 100,
        "customers": 10

    }
    return JsonResponse(data)



class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["eric", "Laura", "Ger","Mairead"]
        data = {
            "labels":labels,
            "values": [10,20,30,40],
            "user": User.objects.all().count(),
            "questions": Question.objects.all().count(),
            "choices":Choice.objects.all().count()
        }
        return Response(data)