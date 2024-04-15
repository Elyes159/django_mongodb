from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required  
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import   LoginForm
from .forms import   LoginForm,LoginFormJ,LoginFormM,AdminForm
from django.contrib.auth import authenticate, login


def home_view(request):
    return render(request, 'home.html')


def loginss_view(request):
    return render(request, 'registration/loginss.html')


def login_juridique_view(request):
    template_name = "logins/jur_login.html"
    form = LoginFormJ(data=request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/responsable-juridique")
    context = {
        "form": form
    }
    return render(request, template_name, context)


def login_maintenance_view(request):
    template_name = "logins/main_login.html"
    form = LoginFormM(data=request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/res_maintenace")
    context = {
        "form": form
    }
    return render(request, template_name, context)

def login_admin_view(request):
    template_name = "logins/admin_login.html"
    form = AdminForm(data=request.POST or None)
    
    if request.method == 'POST':
        
        form = AdminForm(data=request.POST or None)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect("/admin_interface")
            else :
                print("mafamma chay")
    context = {
        "form": form
    }
    return render(request, template_name, context)


def login_user_view(request):
    template_name = "/login.html"
    form = LoginForm(data=request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, template_name, context)
@login_required
def home(request):
 return render(request, "home.html", {})

def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})

def responsable_juridique(request):
    # Logique de vue pour la page du responsable juridique
    return render(request, 'responsable_juridique.html', {})

def res_maintenace(request):
    # Votre logique de vue pour l'interface d'administration
    context = {
        # Mettez ici les données que vous souhaitez transmettre à votre template
    }
    return render(request, 'res_maintenace.html', context)

def admin_interface(request):
    # Votre logique de vue pour l'interface d'administration
    context = {
        # Mettez ici les données que vous souhaitez transmettre à votre template
    }
    return render(request, 'admin_interface.html', context)

def add_site_view(request):
    # Logique de traitement pour l'ajout de nouveaux sites
    if request.method == 'POST':
        # Traitement des données du formulaire et ajout du site à la base de données
        pass  # Remplacez ceci par votre propre logique de traitement
        
        # Redirection vers une page de confirmation ou une autre page appropriée
        return render(request, 'confirmation_page.html')

    # Si la méthode HTTP est GET, simplement rendre la page pour ajouter un site
    return render(request, 'add_site.html')
def add_jui_view(request):
    # Logique de traitement pour l'ajout de nouveaux sites
    if request.method == 'POST':
        # Traitement des données du formulaire et ajout du site à la base de données
        pass  # Remplacez ceci par votre propre logique de traitement
        
        # Redirection vers une page de confirmation ou une autre page appropriée
        return render(request, 'confirmation_page.html')

    # Si la méthode HTTP est GET, simplement rendre la page pour ajouter un site
    return render(request, 'add_jui.html')

def modify_jui(request, codeSite):
    # Votre logique de vue ici
    return render(request, 'modify_jui.html')

def delete_jui(request):
    if request.method == 'GET':
        # Obtenir le code du site à supprimer depuis les paramètres de la requête
        code_site = request.GET.get('code', None)
        
        # Supprimer le site en utilisant le code fourni (c'est un exemple, veuillez adapter selon vos besoins)
        # Exemple : Site.objects.filter(code=code_site).delete()
        
        # Rediriger l'utilisateur vers une autre page après la suppression
        return redirect('responsable_juridique')  # Rediriger vers la page d'accueil par exemple
    else:
        # Si une méthode HTTP autre que GET est utilisée, renvoyer une réponse HTTP 405 (Méthode non autorisée)
        return HttpResponse(status=405)


def admin_interface(request):
    # Votre logique de vue ici
    return render(request, 'admin_interface.html', {})
 
def informations(request):
    # Votre logique de vue ici
    return render(request, 'informations.html', {})

def Colocation(request):
    # Votre logique de vue ici
    return render(request, 'Colocation.html', {})


def Equipment_actifs(request):
    # Votre logique de vue ici
    return render(request, 'Equipment_actifs.html', {})

def O_M(request):
    # Votre logique de vue ici
    return render(request, 'O_M.html', {})

def Energie(request):
    # Votre logique de vue ici
    return render(request, 'Energie.html', {})

def espace (request):
    # Votre logique de vue ici
    return render(request, 'espace .html', {})

def structure (request):
    # Votre logique de vue ici
    return render(request, 'structure.html', {})

def acces(request):
    # Votre logique de vue ici
    return render(request, 'acces.html', {})

def consultant(request):
    # Votre logique de vue ici
    return render(request, 'consultant.html', {})