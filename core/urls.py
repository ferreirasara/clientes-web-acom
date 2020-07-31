from django.urls import path
from .views import index, manager, delete, edit, new, logoutUser, loginUser

urlpatterns = [
    path('', index, name='index'),
    path('manager', manager, name='manager'),
    path('delete/<str:obj>/<int:pk>', delete, name='delete'),
    path('edit/<str:obj>/<int:pk>', edit, name='edit'),
    path('new/<str:obj>', new, name='new'),
    path('logout', logoutUser, name='logout'),
    path('login', loginUser, name='login'),
]
