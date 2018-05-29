from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader, Template, RequestContext
from django.template.loader import render_to_string

# Create your views here.

def index(request):

    latestQuestions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')

    context = {'latestQuestions': latestQuestions}
    return render(request, 'polls/index.html',context)

def eric(request, question_id):
    s2 = '<html><head><title>eric page 1</title></head>' \
        '<body> passed in the url is' \
        + str(question_id) + \
        '<h2>this is erics webpage using django!<h2>' \
        '</body></html>'
    print('eric hit')
    return HttpResponse(s2)

def result(request, question_id):
    print('in result')
    return HttpResponse('result is %s' % question_id)