from django.shortcuts import render, redirect
from .models import Users
def index(request):
    for users in Users.objects.all():
        print(users.__dict__)
    context = {
        'all_users': Users.objects.all()
    }
    return render(request, "index.html", context)