from django.shortcuts import render
from googletrans import Translator
# Create your views here.
def translate(request):
    if request.method == "POST":
            srcs = request.POST.get("src",None)
            txt = request.POST.get("text", None)
            des = request.POST.get("des",None)
            translator = Translator()
            t=translator.translate(txt,src=srcs, dest=des)
            return render(request, 'translate.html', {"result":t.text})
    return render(request,'translate.html')