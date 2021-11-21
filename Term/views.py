from django.shortcuts import redirect, render
from .models import Term, Vocabulary


# Create your views here.


def term(request):
    if request.method == "POST":
        name = request.POST['term']

        newTerm = Term.objects.create(
            term_name=name,
            user=request.user
        )

        newTerm.save()
        return redirect("term")

    terms = Term.objects.all().filter(user_id=request.user.id)
    return render(request, 'term.html', {'count': terms.count(), 'terms': terms})


def delete_term(request, pk):
    term = Term.objects.get(id=pk)
    term.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def edit_term(request, pk):
    term = Term.objects.get(id=pk)
    if request.method == "POST":
        term_name_update = request.POST['term']
        Term.objects.filter(id=pk).update(term_name=term_name_update)
        return redirect('term')

    return render(request, 'edit-term.html', {"term": term})


def vocabulary(request, pk):
    if request.method == "POST":
        word_rq = request.POST['word']
        define_rq = request.POST['define']
        term = pk

        term_current = Term.objects.get(id=term)

        newVocabulary = Vocabulary.objects.create(
            word=word_rq,
            define=define_rq,
            term=term_current
        )
        newVocabulary.save()

    vocabularies = Vocabulary.objects.all().filter(term=pk)
    return render(request, 'vocabulary.html', {"vocabularies": vocabularies})


def delete_vocabulary(request, pk):
    vocabulary = Vocabulary.objects.get(id=pk)
    vocabulary.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def update_vocabulary(request, pk):
    vocabulary = Vocabulary.objects.get(id=pk)
    if request.method == "POST":
        word_update = request.POST['word']
        define_update = request.POST['define']
        Vocabulary.objects.filter(id=pk).update(word=word_update, define=define_update)
        return redirect("vocabulary", vocabulary.term.id)
        # return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'edit-vocabulary.html', {"vocabulary": vocabulary})
