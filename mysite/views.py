from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst','off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
#punctuation remover
    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!()-[]{};:'",\<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'removed punctuations', 'analyzedtext': analyzed}

        djtext =analyzed
#UPPERCASE
    if(capfirst == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Uppercase', 'analyzedtext': analyzed}
        djtext = analyzed
#new line remover
    if(newlineremove == 'on'):
        analyzed = ""
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose':'new line removed' ,'analyzedtext': analyzed}

        djtext = analyzed
 #extra space remover
    if(extraspaceremover == 'on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if (djtext[index] == " " and djtext[index+1]== " "):
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'extra space removed', 'analyzedtext': analyzed}
        return render(request, 'analyze.html', params)
        djtext = analyzed
#character counter:
    if(charcount =='on'):
        start = 0
        for char in (djtext):
            if char!= " ":
                start = start+1

        params = {'purpose': 'character count', 'analyzedtext': start}
    if removepunc !='on' and capfirst!= 'on' and newlineremove!='on' and extraspaceremover!='on' and charcount != 'on':
        return HttpResponse('you have not selected any option')
    return render(request, 'analyze.html', params)










