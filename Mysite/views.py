from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return render(request,'index.html')

def analyze(request):
    #Get the values
    main_text=request.POST.get('text','default')
    a=request.POST.get("remove_punc",'off')
    b=request.POST.get("capitalize",'off')
    c=request.POST.get("newline",'off')
    d = request.POST.get("char_count", 'off')

    if(a=="on" or b=="on" or c=="on" or d=="on"):
         str=""
         if a=="on":
            punctuation='''[]{}-!"#$%&'()*+,./:;<=>?@\^_`|'''
            for char in main_text:
                if char not in punctuation:
                    str=str+char
            params={'purpose':'Removed Punctuations','analyzed_string':str}
            main_text=str

         if b=='on':
            str=main_text.upper()
            params={'purpose':'Capitalized String','analyzed_string':str}
            main_text = str

         if c=="on":
            str=""
            for char in main_text:
                if (char != "\n" and char!="\r"):
                    str=str+char
            params = {'purpose': 'Remove Next Line', 'analyzed_string': str}
            main_text = str

         if d=="on":
            k=0
            str=""
            for char in main_text:
                if char==" ":
                    pass
                else:
                    str=str+char
                    k+=1
            params = {'purpose': 'Character Count', 'analyzed_string': k}
         return render(request,'analyze.html', params)
    else:
        return HttpResponse("Error!!! Please Select a Operation")
