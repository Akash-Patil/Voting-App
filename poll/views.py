from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from poll.models import Question,Choice
#from reg.models import Member
from django.urls import reverse
from django.template import loader

def index(request):                                             #to check latest questions  #home page for voting
    latest_Questions = Question.objects.order_by('-pub_date')[:5] 
    context = {'latest_Questions':latest_Questions}
    return render(request, 'poll/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)   #get objects associated to the questions or else show 404
    return render(request, 'poll/detail.html', {'question': question})

def results(request, question_id):                           # will display results
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)   # handles vote counting
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'poll/detail.html', {'question':question,'error_message':"please select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results',args=(question.id,  )))








