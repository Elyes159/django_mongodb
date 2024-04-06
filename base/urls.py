from django.urls import path, include
from .views import authView, home, admin_interface, responsable_juridique, res_maintenace, add_site_view, add_jui_view, modify_jui, delete_jui


urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin_interface/', admin_interface, name='admin_interface'),
    path('res_maintenace/', res_maintenace, name='res_maintenace'),
    path('responsable-juridique/', responsable_juridique, name='responsable_juridique'),
    path('add_site/', add_site_view, name='add_site'),  
    path('add_jui/', add_jui_view, name='add_jui'),
    path('modify_jui/', modify_jui, name='modify_jui'),
    path('delete_jui/', delete_jui, name='delete_jui'),     
]




