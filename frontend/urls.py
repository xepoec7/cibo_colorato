from django.urls import path
from . import views


app_name = 'frontend'


urlpatterns = [
	path('', views.home_page, name='home'),
	path('kiosk/', views.kiosk_page, name='kiosk'),
	path('menu/', views.menu_page, name='menu'),
	path('menu/ajax/<int:cat_id>/', views.ajax_menu_nav, name="ajax_menu_nav"),
]