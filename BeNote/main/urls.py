from django.urls import path

from .views import *

urlpatterns = [
    path('', BeNoteMain.as_view(), name='main'),
    path('newnote/', New_note, name='newnote'),
    path('notes/', notes, name='notes'),
    path('login/',Login_user.as_view(), name='login'),
    path('registration/', UserRegister.as_view(), name='registration'),
    path('logout/', Logout.as_view(), name='logout')
]