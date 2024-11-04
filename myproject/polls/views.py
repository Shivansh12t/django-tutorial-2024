from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Question
# from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list" : latest_question_list
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.query.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("question does not exist")
    return render(request, "polls/detail.html", {"question" : question})a

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
