from django.shortcuts import render

INDEX_HTML = '/Users/jbalkovec/Desktop/CPSC/CPSC 3300/Q_Project/goal_garden/myapp/templates/index.html'

def index(request):
    return render(request, INDEX_HTML)