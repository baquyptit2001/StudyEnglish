from django.shortcuts import render

# Create your views here.
from Game.models import Question


def home(request):
    return render(request, 'index.html')


def add_question(request):
    text = ''
    print(request.user.is_superuser)
    if request.method == "POST":
        question = Question.objects.create(
            name=request.POST['question'],
        )
        status = 'true'
        if question is not None:
            for ans in request.POST['answer']:
                question.answer.create(
                    answer=ans,
                    status=status
                )
                status = 'false'
        text = request.POST['question']
    return render(request, 'add-question.html', {"text": text})
