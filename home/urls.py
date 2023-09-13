from django.urls import path
from home import views


urlpatterns = [
    path('fecha/', views.fecha),
    path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento),
    path('hola/', views.hola),
    path('mi-template/', views.mi_template),
    path('mi-template/<str:nombre>', views.tu_template),
    path('prueba-template/', views.prueba_template),
    path('ver-personas/', views.ver_persona),
    path('crear-personas/<str:nombre>/<str:apellido>/', views.crear_persona),
]
