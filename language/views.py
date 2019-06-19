from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question, Phrase, Burarra
import random
from .forms import TextForm
from django.shortcuts import redirect
# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'language/index.html', context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'language/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'language/results.html', {'question': question})

phrase = random.choice(Phrase.objects.all())

def burarra(request):
    global phrase

    if request.method == 'POST':
            form_p = TextForm(request.POST)
            if form_p.is_valid():
                print(form_p.cleaned_data['translation'])
                burarra_translation = Burarra.objects.create(phrase=phrase, translation_text=form_p.cleaned_data['translation'])
                burarra_translation.save()
                phrase = random.choice(Phrase.objects.all())
                form = TextForm(request.POST)
                context = {
                'phrase' : phrase,
                'form':form
                }
                #return render(request, 'language/burarra.html', context)
                return redirect('/language/burarra')

    phrase = random.choice(Phrase.objects.all())
    form = TextForm(request.POST)
    context = {
    'phrase' : phrase,
    'form':form
    }        
    return render(request, 'language/burarra.html', context)

def warlpiri(request):
    context = {
    }
    return render(request, 'language/warlpiri.html', context)


class IndexView(generic.ListView):
    template_name = 'language/index.html'
    # overriding automatic variable name ("question_list")
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'language/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'language/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'language/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('language:results', args=(question.id,)))