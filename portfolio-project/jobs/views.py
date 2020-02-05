from django.shortcuts import render


def homepage(request):
    return render(request, 'jobs/home.html')
