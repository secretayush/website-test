from django.shortcuts import render
import json

# Create your views here.
def user_info(request):
    return render(request,'home/home.html')

def user_team(request):
    json_data = open('static/home/file.json')

    context ={
        'posts': json.load(json_data)
    }
    return render(request,'home/team.html',context)

def user_about(request):
    return render(request,'home/index.html')
def user_contact(request):
    return render(request,'home/index.html')