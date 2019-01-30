from django.contrib import admin
from django.urls import path
from core import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar_cadastro/', views.listar_cadastro, name='listar_cadastro'),
]
