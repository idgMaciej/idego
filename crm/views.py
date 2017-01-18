from django.shortcuts import render
from .forms import CreateCompany, RemoveUser
from .models import Company
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='http://127.0.0.1:8000/')
def companies(request):
    if request.method == 'POST':
        form = CreateCompany(request.POST)
        if form.is_valid():
            company = form.save()
            company.save()
            return redirect('companies')
    else:
        form = CreateCompany()
    company = Company.objects.order_by('-add_date')[:]
    context = {'form': form, 'companies': company}
    return render(request, 'companies.html', context)


@login_required(login_url='http://127.0.0.1:8000/')
def remove_user(request):
    if request.method == 'POST':
        form = RemoveUser(request.POST)
        username = request.POST.get('username')
        if form.is_valid():
            rem = User.objects.get(username=username)
            rem.delete()
            return redirect('users')
        else:
            return redirect('users')
    else:
        form = RemoveUser()
        context = {'form': form}
        return render(request, 'remove_user.html', context)


@login_required(login_url='http://127.0.0.1:8000/')
def main(request):
    return render(request, 'main.html')


@login_required(login_url='http://127.0.0.1:8000/')
def users(request):
    user = User.objects.all()
    return render(request, 'users.html', {'users': user})
