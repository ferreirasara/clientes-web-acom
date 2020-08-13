from django.urls import path
from .views import index, manager, logoutUser, loginUser, update, verify, notes
from .views import newNote, newPort, newClient, newSystem
from .views import editNote, editPort, editClient, editSystem
from .views import deleteNote, deletePort, deleteClient, deleteSystem


urlpatterns = [
    path('', index, name='index'),
    path('update', update, name='update'),
    path('verify', verify, name='verify'),
    path('logout', logoutUser, name='logout'),
    path('login', loginUser, name='login'),

    path('manager', manager, name='manager'),
    path('manager/client/new', newClient, name='newClient'),
    path('manager/port/new', newPort, name='newPort'),
    path('manager/system/new', newSystem, name='newSystem'),
    path('manager/client/delete/<int:idClient>', deleteClient, name='deleteClient'),
    path('manager/port/delete/<int:idPort>', deletePort, name='deletePort'),
    path('manager/system/delete/<int:idSystem>', deleteSystem, name='deleteSystem'),
    path('manager/client/edit/<int:idClient>', editClient, name='editClient'),
    path('manager/port/edit/<int:idPort>', editPort, name='editPort'),
    path('manager/system/edit/<int:idSystem>', editSystem, name='editSystem'),

    path('notes', notes, name='notes'),
    path('notes/new', newNote, name='newNote'),
    path('notes/edit/<int:idNote>', editNote, name='editNote'),
    path('notes/delete/<int:idNote>', deleteNote, name='deleteNote'),
]

