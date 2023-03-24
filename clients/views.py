from django.shortcuts import render
from .models import UserList

def user_list(request):
    clients = UserList.objects.all()
    return render(request, 'index.html', {'clients': clients})
