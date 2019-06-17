from django.shortcuts import render


def tachyon(request):
    return render(request, 'tachyon.html')
