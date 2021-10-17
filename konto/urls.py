from django.urls import path
from . import views

app_name = 'konto'

urlpatterns = [
	path('einlogen/', views.login_page, name='login'),
	path('auslogen/', views.logout_request, name='logout'),
]