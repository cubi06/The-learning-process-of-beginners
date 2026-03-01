"""
URL configuration for quzhi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from TestModel import views
urlpatterns = [
    path("home/",views.visual_home),
    path('login/',views.visual_login),
    path('register/',views.visual_register),
    path('login_form/',views.login_form),
    path('newtasks/',views.newtasks),
    path('newtodos/',views.newtodos),
    path('task-complete/',views.task_complete),
    path('infochange/',views.infochange),
    path('logout/',views.logout),
    path('visualization/',views.visualization),
    path('delete_task/',views.delete_task),
    path('visualization/todo_list/',views.visual_todo_lists),
    path('delete_todo/',views.delete_todo),
    path('visualization/displaytree/',views.visual_displaytree),
    path('visualization/pinechart/',views.visual_pinechart),
    path('npcchoice/<int:id>/',views.npc_choice),
    path('dialog/',views.npc_dialog),
    path('clear-chat/',views.clear_chat)
]

