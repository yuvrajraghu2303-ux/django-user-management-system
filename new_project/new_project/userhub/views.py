from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import User


def hello(request):
    return HttpResponse("Hello World!")


def user_list(request):
    users = User.objects.all().order_by('id')
    return render(request, 'userhub/user_list.html', {'users': users})


def new_user(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        role = request.POST.get('role', '').strip()

        if not name or not email or not role:
            return HttpResponse("Please fill in all fields.", status=400)

        User.objects.create(name=name, email=email, role=role)
        return redirect('user_list')

    return render(request, 'userhub/new_user.html')


def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'userhub/user_detail.html', {'user': user})


def about(request):
    return HttpResponse("This is the About Page.")
