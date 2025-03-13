from django.shortcuts import render
from .models import User

def user_list(request):
    users = User.objects.all()
    return render(request, 'myapp/user_list.html', {'users': users})
