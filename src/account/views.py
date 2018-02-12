from django.shortcuts import render


def index(request):
    message = 'Hello from the account app!'

    return render(request, 'account/base.html', {'message': message, })
