from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

# displays the current questions
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list': question_list}
    return render(request, 'polls/index.html', context)

# this will show details about specific questions
# "question_id" comes from the url as a parameter
def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Selected question not found.")
  return render(request, 'polls/detail.html', { 'question': question })

# Get the question selected and display the voting results
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', { 'question': question })

# Vote for a question choice
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Handle no choice selected, show the question and the error message
        # Error message handler is defined in detail template
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # If a choice was found, update the choice with a new vote
        selected_choice.votes += 1
        selected_choice.save()
        # Whenever successful POST happens, redirect to base url
        # This prevents more data from being sent if the back button is pressed
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))