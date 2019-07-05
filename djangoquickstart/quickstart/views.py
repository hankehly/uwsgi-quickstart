from django.shortcuts import render


def welcome(request):
    message = request.GET.get('message')
    return render(request, 'quickstart/welcome.html', {'message': message})
