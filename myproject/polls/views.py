from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, you're at polls")
# Create your views here.

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")

def results(request, question_id):
    response = "You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("You're voting on question {question_id}.")
