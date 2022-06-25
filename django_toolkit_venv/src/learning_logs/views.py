from django.shortcuts import render # import render function to render resopnses based on data from views

# Create your views here.

def index(request):
    """Learning Log Home Page"""
    # render function has two arguments - request from a url and a template 
    # it uses to build the page
    return render(request, 'templates/learning_logs/index.html')
