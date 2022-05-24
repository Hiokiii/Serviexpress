from django.urls import path
from .views import home, iniciar_sesion, productos

urlpatterns = [
    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
]