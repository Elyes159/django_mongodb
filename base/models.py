from django.db import models

class MonModele(models.Model):
    champ_texte = models.CharField(max_length=100)
    champ_entier = models.IntegerField(default=0)  # Ajoutez le champ avec une valeur par défaut
    # Autres champs...
