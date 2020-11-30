from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render(request, "index.html")


def resultpage(request):
    rtext = request.POST.get('textcontent', 'default')
    itext = rtext
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    removeline = request.POST.get('removeline', 'off')
    removespaces = request.POST.get('removespaces', 'off')
    countchar = request.POST.get('countchar', 'off')
    rvalue = ''
    if (removepunc == 'on' or removespaces == 'on' or uppercase == 'on' or removeline == 'on' or removespaces == 'on' or countchar == 'on'):
        if removepunc == 'on':
            punc = string.punctuation
            for char in rtext:
                if char not in punc:
                    rvalue = rvalue+char
            rtext = rvalue

        if uppercase == 'on':
            rvalue = rtext.upper()
            rtext = rvalue

        if removeline == 'on':
            rvalue = ''
            for char in rtext:
                if char != '\n' and char != '\r':
                    rvalue = rvalue+char

                rtext = rvalue

        if countchar == 'on':
            for index, char in enumerate(rtext):
                index = index
            rvalue = index
            rtext = rvalue

        if removespaces == 'on':
            if ('  ') in rtext:
                rvalue = rtext.replace("  ", '')
            else:
                rvalue = rtext
            rtext = rvalue

        params = {'result': rvalue, 'input': itext}

        return render(request, 'result.html', params)
    else:
        return HttpResponse("<h1>Please choose an operation to perform</h1>")
