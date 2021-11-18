from typing import Text
from django.shortcuts import render
from googletrans import Translator
from Translate.models import Languages

# Create your views here.
def translate(request):
    languages=Languages.objects.all()
    if request.method == "POST":
            txt = request.POST.get("text", None)
            srcs = str(request.POST.get("src",None))
            srcs1=(srcs.split('-'))[0]
            if srcs=='zh-CN':
                   srcs1='zh-CN'
            des = request.POST.get("des",None)
            des1=(des.split('-'))[0]
            context={"srcs":srcs,"des":des}
            if des=='zh-CN':
                    des1='zh-CN'
            if txt == "":
                    return render(request, 'translate.html', {"input":"","output":"","context":context,"languages":languages})
            translator = Translator()
            t=translator.translate(txt,src=srcs1, dest=des1)
            
            return render(request, 'translate.html', {"input":txt,"output":t.text,"context":context,"languages":languages})
    return render(request,'translate.html', {"languages":languages})