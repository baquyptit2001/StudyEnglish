from django.shortcuts import render
from googletrans import Translator
# Create your views here.
def translate(request):
    if request.method == "POST":
            srcs = str(request.POST.get("src",None))
            srcs=(srcs.split('-'))[0]
            txt = request.POST.get("text", None)
            
            des = request.POST.get("des",None)
            des=(des.split('-'))[0]
            translator = Translator()
            t=translator.translate(txt,src=srcs, dest=des)
            context={"srcs":srcs,"des":des}
            return render(request, 'translate.html', {"input":txt,"output":t.text,"context":context})
    return render(request,'translate.html')