from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'flip/index.html')
# def index(request):
#     return HttpResponse("hiiiii")
def detail(request):
    return render(request, 'flip/detail.html')
def written(request, post_id):
    return HttpResponse(f"hiii{post_id}")

def old_url_redirect(request):
    return redirect(reverse('flip:new_url_1'))

def new_url_view(request):
    return HttpResponse('this is new url')