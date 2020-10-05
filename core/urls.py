from django.urls import path
from .views import index, logoutUser, loginUser, update, notes
from .views import managerClient, managerPort, managerSystem, managerServer
from .views import newNote, newPort, newClient, newSystem, newServer
from .views import editNote, editPort, editClient, editSystem, editServer
from .views import deleteNote, deletePort, deleteClient, deleteSystem, deleteServer
from .views import viewNote


urlpatterns = [
    path('', index, name='index'),
    path('update', update, name='update'),
    path('logout', logoutUser, name='logout'),
    path('login', loginUser, name='login'),

    path('manager/client', managerClient, name='managerClient'),
    path('manager/port', managerPort, name='managerPort'),
    path('manager/system', managerSystem, name='managerSystem'),
    path('manager/server', managerServer, name='managerServer'),

    path('manager/client/new', newClient, name='newClient'),
    path('manager/port/new', newPort, name='newPort'),
    path('manager/system/new', newSystem, name='newSystem'),
    path('manager/server/new', newServer, name='newServer'),

    path('manager/client/delete/<int:idClient>', deleteClient, name='deleteClient'),
    path('manager/port/delete/<int:idPort>', deletePort, name='deletePort'),
    path('manager/system/delete/<int:idSystem>', deleteSystem, name='deleteSystem'),
    path('manager/server/delete/<int:idServer>', deleteServer, name='deleteServer'),

    path('manager/client/edit/<int:idClient>', editClient, name='editClient'),
    path('manager/port/edit/<int:idPort>', editPort, name='editPort'),
    path('manager/system/edit/<int:idSystem>', editSystem, name='editSystem'),
    path('manager/server/edit/<int:idServer>', editServer, name='editServer'),

    path('notes', notes, name='notes'),
    path('notes/new', newNote, name='newNote'),
    path('notes/<int:idNote>', viewNote, name='viewNote'),
    path('notes/edit/<int:idNote>', editNote, name='editNote'),
    path('notes/delete/<int:idNote>', deleteNote, name='deleteNote'),
]

