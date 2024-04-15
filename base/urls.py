from django.urls import path, include
from .views import authView, home, admin_interface, responsable_juridique 
from .views import  res_maintenace, add_site_view, add_jui_view, modify_jui, delete_jui
from . import views
from .views import home_view 
from .views import O_M , Energie , espace , structure , acces , consultant
from .views import informations, Colocation, Equipment_actifs

urlpatterns = [

    path("signup/", authView, name="authView"),
    path('', home_view, name='home'),  
    path('home/', views.home_view, name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin_interface/', admin_interface, name='admin_interface'),
    path('res_maintenace/', res_maintenace, name='res_maintenace'),
    path('responsable-juridique/', responsable_juridique, name='responsable_juridique'),
    path('add_site/', add_site_view, name='add_site'),  
    path('add_jui/', add_jui_view, name='add_jui'),
    path('modify_jui/', modify_jui, name='modify_jui'),
    path('delete_jui/', delete_jui, name='delete_jui'),   
    path('accounts/login/', views.login_user_view),
    path('informations/', informations, name='informations'),
    path('Colocation/', Colocation, name='Colocation'),
    path('Equipment_actifs/', Equipment_actifs, name='Equipment_actifs'),
    path('O_M/', O_M, name='O_M'),
    path('Energie/', Energie, name='Energie'),
    path(' espace/', espace , name='espace'), 
    path('structure /', structure  , name='structure'), 
    path('acces /', acces  , name='acces'),
    path('consultant /', consultant , name='consultant'),
    
    
]     
