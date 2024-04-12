from django.urls import path, include
from .views import authView, home, admin_interface, responsable_juridique
from .views import  res_maintenace, add_site_view, add_jui_view, modify_jui, delete_jui,login_juridique_view,loginss_view,login_admin_view
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin_interface/', admin_interface, name='admin_interface'),
    path('res_maintenace/', res_maintenace, name='res_maintenace'),
    path('responsable-juridique/', responsable_juridique, name='responsable_juridique'),
    path('add_site/', add_site_view, name='add_site'),  
    path('add_jui/', add_jui_view, name='add_jui'),
    path('modify_jui/', modify_jui, name='modify_jui'),
    path('delete_jui/', delete_jui, name='delete_jui'),   
    path('accounts/login/', views.login_user_view),
    path('login/ResponsableJuridique/',views.login_juridique_view,name="login_responsable_juridique"),#hedha lien mta3 login de responsable juridique
    path('login/ResponsableManitenance/',views.login_maintenance_view,name="login_maintenance_view"),
    path('loginss/',views.loginss_view), # lien bech te5tar en tant que chkoun bech taamel login
    path('login/Adiministrator',views.login_admin_view,name = "login_admin_view")
]




