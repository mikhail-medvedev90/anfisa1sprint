from django.shortcuts import render


def description(request):
    template = 'about.html'
    return render(request, template)
