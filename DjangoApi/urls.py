from django.urls import path
from api.login.login_view import login_views, registrar_views, recuperar_views, salir_view
from api.home.home_view import home_views

urlpatterns = [
    path('login/', login_views, name='login_vista'),
    path('salir/', salir_view, name='salir'),
    path('registro/', registrar_views, name='registro_vista'),
    path('recuperar/', recuperar_views, name='recuperar'),
    path('', home_views, name='home'),
    path('home/', home_views, name='home'),
]
