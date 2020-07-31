from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Client, Port, System
from .forms import PortForm, SystemForm, ClientForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('index')


def index(request):
    if str(request.user) != 'AnonymousUser':
        context = {
            'clients': Client.objects.all(),
            'ports': Port.objects.exclude(id__in=Client.objects.all())
        }
        return render(request, 'index.html', context)
    else:
        return loginUser(request)


def manager(request):
    if str(request.user) != 'AnonymousUser':
        context = {
            'clients': Client.objects.all(),
            'ports': Port.objects.all(),
            'systens': System.objects.all()
        }
        return render(request, 'manager.html', context)
    else:
        return loginUser(request)


def delete(request, obj, pk):
    if str(request.user) != 'AnonymousUser':
        if obj == 'p':
            Port.objects.get(pk=pk).delete()
        elif obj == 's':
            System.objects.get(pk=pk).delete()
        elif obj == 'c':
            Client.objects.get(pk=pk).delete()

        return redirect('manager')
    else:
        return loginUser(request)


def edit(request, obj, pk):
    if str(request.user) != 'AnonymousUser':
        if obj == 'p':
            instance = get_object_or_404(Port, id=pk)
            form = PortForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('manager')
            return render(request, 'edit-port.html', {'form': form})
        elif obj == 's':
            instance = get_object_or_404(System, id=pk)
            form = SystemForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('manager')
            return render(request, 'edit-system.html', {'form': form})
        elif obj == 'c':
            instance = get_object_or_404(Client, id=pk)
            form = ClientForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('manager')
            return render(request, 'edit-client.html', {'form': form})
    else:
        return loginUser(request)


def new(request, obj):
    if str(request.user) != 'AnonymousUser':
        if obj == 'p':
            if str(request.method) == 'POST':
                form = PortForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('manager')
                else:
                    return render(request, 'edit-client.html', {'form': PortForm()})
            else:
                return render(request, 'edit-port.html', {'form': PortForm()})
        elif obj == 's':
            if str(request.method) == 'POST':
                form = SystemForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('manager')
                else:
                    return render(request, 'edit-client.html', {'form': SystemForm()})
            else:
                return render(request, 'edit-system.html', {'form': SystemForm()})
        elif obj == 'c':
            if str(request.method) == 'POST':
                form = ClientForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('manager')
                else:
                    return render(request, 'edit-client.html', {'form': ClientForm()})
            else:
                return render(request, 'edit-client.html', {'form': ClientForm()})
    else:
        return loginUser(request)
