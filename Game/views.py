from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'index.html')


def add_question(request):
    text = ''
    print(request.user.is_superuser)
    if request.method == "POST":
        print(request.POST)
        text = request.POST['question']
    return render(request, 'add-question.html', {"text": text})
