from django.shortcuts import render

# Create your views here.
def ErrorPage(request):
    return render(request, 'ErrorPage/index.html')