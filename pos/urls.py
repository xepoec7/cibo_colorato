from django.urls import path
from . import views

app_name = 'pos'

urlpatterns = [
	path('', views.pos_page, name='pos'),
	path('check/', views.pos_check, name='pos_check'),
	path('gesendet/', views.pos_sent, name='pos_sent'),
	path('nachricht/', views.pos_msg, name='pos_msg'),
	path('ajax/', views.pos_ajax, name='pos_ajax'),
	path('ajax/<str:type>/<int:id>/', views.pos_ajax, name='pos_ajax'),
	path('ajax/<str:type>/<int:id>/<int:qty>/', views.pos_ajax, name='pos_ajax'),
	path('ajax/cart/', views.cart_ajax, name='cart_ajax'),
	path('ajax/cart/remove/<int:id>/', views.cart_remove, name='cart_remove'),
]