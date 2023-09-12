"""
URL configuration for taskmanager_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from tasks import views



urlpatterns = [
    path('listar_tarefas/', views.listar_tarefas, name='listar_tarefas'),
    path('adicionar_tarefa/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('marcar_como_concluida/<int:pk>/', views.marcar_como_concluida, name='marcar_como_concluida'),
    path('excluir_tarefa/<int:pk>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('remover_tarefa/<int:pk>/', views.remover_tarefa, name='remover_tarefa'),

]
