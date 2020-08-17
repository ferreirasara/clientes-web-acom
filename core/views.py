from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from .models import Client, Port, System, Note
from django.http import HttpResponseRedirect
from .forms import PortForm, SystemForm, ClientForm, UpdateForm, NoteForm, SearchForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime
import requests


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
            'clients': Client.objects.all().order_by('name'),
            'ports': Port.objects.filter(status=1).order_by('connector'),
            'form': SearchForm()
        }
        if str(request.method) == 'POST':
            context['form'] = SearchForm(request.POST)
            if context['form'].is_valid():
                search = context['form'].data['search']
                context['clients'] = Client.objects.filter(name__contains=search).order_by('name')
                return render(request, 'index.html', context)
            else:
                return render(request, 'index.html', context)
        else:
            return render(request, 'index.html', context)
    else:
        return loginUser(request)


def notes(request):
    if str(request.user) != 'AnonymousUser':
        context = {
            'notes': Note.objects.all()
        }
        return render(request, 'notes.html', context=context)
    else:
        return loginUser(request)


def newNote(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = NoteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('notes')
            else:
                return render(request, 'edit-note.html', {'form': form})
        else:
            return render(request, 'edit-note.html', {'form': NoteForm()})
    else:
        return loginUser(request)


def editNote(request, idNote):
    if str(request.user) != 'AnonymousUser':
        instance = get_object_or_404(Note, id=idNote)
        form = NoteForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('notes')
        return render(request, 'edit-note.html', {'form': form})
    else:
        return loginUser(request)


def deleteNote(request, idNote):
    if str(request.user) != 'AnonymousUser':
        Note.objects.get(pk=idNote).delete()
        return redirect('notes')
    else:
        return loginUser(request)


def update(request):
    if str(request.user) != 'AnonymousUser':
        if request.method == 'POST':
            form = UpdateForm(request.POST)
            if form.is_valid():
                clients = Client.objects.filter(system_id=form.data['systemId'])
                for client in clients:
                    client.version = datetime.strptime(form.data['date'], '%d/%m/%Y').date()
                    client.save()
                return redirect('index')
        else:
            form = UpdateForm()
            return render(request, 'update.html', {'form': form})
    else:
        return loginUser(request)


def verifyClients(request):
    clients = Client.objects.filter(status=1)
    clientsWithError = []
    for client in clients:
        try:
            r = requests.get(client.link)
            if (r.text.find('<html>')) == -1:
                clientsWithError.append(client)
        except:
            clientsWithError.append(client)
    if len(clientsWithError) == 0:
        storage = messages.get_messages(request)
        storage.used = True
        messages.add_message(request, messages.SUCCESS, 'Todos os links estão funcionando.')
    else:
        text = 'Alguns links não estão funcionando: '
        for client in clientsWithError:
            text += '[' + client.system.initials + '_' + client.name + '] '
        storage = messages.get_messages(request)
        storage.used = True
        messages.add_message(request, messages.ERROR, text)
    return redirect('index')


def manager(request):
    if str(request.user) != 'AnonymousUser':
        context = {
            'clients': Client.objects.all().order_by('name'),
            'ports': Port.objects.all().order_by('connector'),
            'systens': System.objects.all().order_by('initials')
        }
        return render(request, 'manager.html', context)
    else:
        return loginUser(request)


def deleteClient(request, idClient):
    if str(request.user) != 'AnonymousUser':
        Client.objects.get(pk=idClient).delete()
        return redirect('manager')
    else:
        return loginUser(request)


def deletePort(request, idPort):
    if str(request.user) != 'AnonymousUser':
        Port.objects.get(pk=idPort).delete()
        return redirect('manager')
    else:
        return loginUser(request)


def deleteSystem(request, idSystem):
    if str(request.user) != 'AnonymousUser':
        System.objects.get(pk=idSystem).delete()
        return redirect('manager')
    else:
        return loginUser(request)


def editClient(request, idClient):
    if str(request.user) != 'AnonymousUser':
        instance = get_object_or_404(Client, id=idClient)
        form = ClientForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            port = get_object_or_404(Port, id=instance.port_id)
            port.status = 2
            port.save()
            nextPage = request.POST['previousPage']
            return HttpResponseRedirect(nextPage)
        return render(request, 'edit-client.html', {'form': form})
    else:
        return loginUser(request)


def editPort(request, idPort):
    if str(request.user) != 'AnonymousUser':
        instance = get_object_or_404(Port, id=idPort)
        form = PortForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            nextPage = request.POST['previousPage']
            return HttpResponseRedirect(nextPage)
        return render(request, 'edit-port.html', {'form': form})
    else:
        return loginUser(request)


def editSystem(request, idSystem):
    if str(request.user) != 'AnonymousUser':
        instance = get_object_or_404(System, id=idSystem)
        form = SystemForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            nextPage = request.POST['previousPage']
            return HttpResponseRedirect(nextPage)
        return render(request, 'edit-system.html', {'form': form})
    else:
        return loginUser(request)


def newClient(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ClientForm(request.POST)
            if form.is_valid():
                client = form.save()
                port = get_object_or_404(Port, id=client.port_id)
                port.status = 2
                port.save()
                return redirect('manager')
            else:
                return render(request, 'edit-client.html', {'form': ClientForm()})
        else:
            return render(request, 'edit-client.html', {'form': ClientForm()})
    else:
        return loginUser(request)


def newPort(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = PortForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('manager')
            else:
                return render(request, 'edit-client.html', {'form': PortForm()})
        else:
            return render(request, 'edit-port.html', {'form': PortForm()})
    else:
        return loginUser(request)


def newSystem(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = SystemForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('manager')
            else:
                return render(request, 'edit-client.html', {'form': SystemForm()})
        else:
            return render(request, 'edit-system.html', {'form': SystemForm()})
    else:
        return loginUser(request)
