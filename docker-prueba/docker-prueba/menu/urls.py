from django.urls import path
from .views import mostrar_menu, guardar_platillo, eliminar_platillo, actualizar_platillo

urlpatterns = [
    path('', mostrar_menu),
    path('agregar/', guardar_platillo, name='guardar_platillo'),
    path('eliminar/<int:comida_id>/', eliminar_platillo, name='eliminar_platillo'),
    path('actualizar/<int:comida_id>/', actualizar_platillo, name='actualizar_platillo')
]