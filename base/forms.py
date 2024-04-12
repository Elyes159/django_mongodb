from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.models import User

from base.models import ResponsableJuridique, ResponsableMaintenance
from django import forms
from .models import Admin


class LoginForm(AuthenticationForm) :
    class Meta :
        model = User
        fields = [ 
            "username",
            "password"
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].label = ''
        # self.fields['password1'].label = ''
        self.fields['username'].help_text = ''
        self.fields['password'].help_text = ''
        self.fields['username'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Username"})
        self.fields['password'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Password", "data-toggle":"password"})
        
        
class LoginFormJ(AuthenticationForm) :
    class Meta :
        model = ResponsableJuridique
        fields = [ 
            "username",
            "password"
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].label = ''
        # self.fields['password1'].label = ''
        self.fields['username'].help_text = ''
        self.fields['password'].help_text = ''
        self.fields['username'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Username"})
        self.fields['password'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Password", "data-toggle":"password"})
        
class LoginFormM(AuthenticationForm) :
    class Meta :
        model = ResponsableMaintenance
        fields = [ 
            "username",
            "password"
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].label = ''
        # self.fields['password1'].label = ''
        self.fields['username'].help_text = ''
        self.fields['password'].help_text = ''
        self.fields['username'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Username"})
        self.fields['password'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Password", "data-toggle":"password"})
        
        

class AdminForm(AuthenticationForm) :
    class Meta :
        model = Admin
        fields = [ 
            "username",
            "password"
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].label = ''
        # self.fields['password1'].label = ''
        self.fields['username'].help_text = ''
        self.fields['password'].help_text = ''
        self.fields['username'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Username"})
        self.fields['password'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Password", "data-toggle":"password"})