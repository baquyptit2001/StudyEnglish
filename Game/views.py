from django.shortcuts import render

# Create your views here.
from Game.models import Question, Answer


def home(request):
    question = Question.objects.order_by('?')[0]
    answer = question.answer_set.order_by('?')
    return render(request, 'index.html', {"question": question, 'answer': answer})


def add_question(request):
    text = ''
    print(request.user.is_superuser)
    if request.method == "POST":
        question = Question.objects.create(
            name=request.POST['question'],
        )
        question.save()
        status = 'true'
        if question is not None:
            for i in range(1, 5):
                Answer.objects.create(
                    question=question,
                    answer=request.POST['answer' + str(i)],
                    status=status
                )
                question.save()
                status = 'false'
        text = request.POST['question']
    return render(request, 'add-question.html', {"text": text})
