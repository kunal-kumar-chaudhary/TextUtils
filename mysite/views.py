# this file has been created by kunal. it was not at all given in advance.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):   
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    # we will see whether the checkbox is 'on' or 'off'?
    # this line of code below will return whether the checkbox is 'on' or 'off'
    '''
    below line of code will check checkbox values
    '''
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremover', 'off')

    print(removepunc)
    # analyze the text
    print(djtext)

    '''
    below line of code will check which checkbox is selected
    '''

    if removepunc == 'on':

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        
        params = {'purpose':'remove punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if fullcaps=='on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'chnaged to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if newlineremove =='on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'new line removed', 'analyzed_text': analyzed}
        
    
    if (removepunc!='on' and fullcaps!='on' and newlineremove!='on'):
        return HttpResponse('for god sake, please select the operation you want to perform!')

    return render(request, 'analyze.html', params)
        


