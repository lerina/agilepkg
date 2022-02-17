from django.shortcuts import render
from django.http import JsonResponse

from django.http import HttpResponse
import json # just for demo old style in ajaxtest()

def echo(request):
    c= {'title':"Ajax - demo"}
    return render(request, 'echo/index.html', c)

def ajaxtest(request):
    """ showing two ways to return json """
    theText = request.POST['text']
    if theText and request.is_ajax:
        return JsonResponse({'theText':theText}) # since dj 1.7
    return HttpResponse(json.dumps({'theText':"You didn't type anything."}), content_type='application/json') # old way

