from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def john_mc(request):
    return render(request, 'home/johnmc.html')


def about(request):
    return render(request, 'home/about.html')
