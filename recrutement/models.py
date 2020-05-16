from django.db import models
from enseignement.models import Localite
from gestion.models import Grade, Domaine, Enseignant
from tinymce import HTMLField
from PIL import Image
from django.db.models.query import QuerySet
from django_group_by import GroupByMixin
from django.urls import reverse
# Create your models here.
from gestion.validators import validate_file_extension_for_image,validate_file_extension_for_document


#################################################################################################################################################
#################################################################################################################################################

class Recrutement(models.Model):
    """Model definition for Recrutement."""

    # TODO: Define fields here
    intitule = models.CharField(max_length=30)
    objet = HTMLField('objet du recrutement')
    ouverture = models.DateTimeField(auto_now=False, auto_now_add=False, help_text="Date d'ouverture")
    fermeture = models.DateTimeField(auto_now=False, auto_now_add=False, help_text="Date de fermeture")
    cible = HTMLField('public cible')
    methode_evaluation = HTMLField("methode d'evaluation")
    date_debut_passage =  models.DateTimeField(auto_now=False, auto_now_add=False, help_text="Debut des passages devant le jury")
    date_fin_passage = models.DateTimeField(auto_now=False, auto_now_add=False, help_text="Fin des passages devant le jury")
    resultat = models.DateTimeField(auto_now=False, auto_now_add=False, help_text="Date de publication des resultats")
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Recrutement."""

        verbose_name = 'Recrutement'
        verbose_name_plural = '  Recrutements'
        ordering = ['-created']
       
    

    def __str__(self):
        """Unicode representation of Recrutement."""
        return self.intitule


    def get_absolute_url(self):
        """Return absolute url for Recrutement."""
        return (reverse("site-home", kwargs={"pk": self.pk}),reverse("recrutement-home", kwargs={"pk": self.pk}),) # 

    # TODO: Define custom methods here
######################################################################################################################################################
######################################################################################################################################################

class DossierRecrutement(models.Model):
    """Model definition for DossierRecrutement."""
    sexe_choice =  (
        ('H', 'Homme',),
        ('F', 'Femme',),
    )
    recrutement = models.ForeignKey(Recrutement, on_delete=models.CASCADE)
    nom         = models.CharField( max_length=50)
    prenom = models.CharField( max_length=50)
    sexe =  models.CharField( max_length=1,choices=sexe_choice,)
    date_de_naissance = models.DateField(auto_now=False, auto_now_add=False, help_text="Date de naissance")
    localite = models.ForeignKey(Localite, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=8)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    domaine = models.ManyToManyField(Domaine, related_name="competence_candidat")
    photo             = models.FileField(upload_to ='recrutement/photos/',default='none.png',validators=[validate_file_extension_for_image]) 
    piece_indentite   = models.FileField(upload_to ='recrutement/pieces/',default='none.png',validators=[validate_file_extension_for_document])
    lettre_motivation = models.FileField(upload_to ='recrutement/lettres/',default='none.png',validators=[validate_file_extension_for_document]) 
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for DossierRecrutement."""

        verbose_name = 'DossierRecrutement'
        verbose_name_plural = 'DossierRecrutements'
        ordering = ['-created']

    def __str__(self):
        """Unicode representation of DossierRecrutement."""
        return "{} {}".format(self.nom, self.prenom)


    def get_absolute_url(self):
        """Return absolute url for DossierRecrutement."""
        return (reverse("jury-dossier", kwargs={"pk": self.pk})) # 


    # TODO: Define custom methods here
#####################################################################################################################################################
#####################################################################################################################################################

class Diplome(models.Model):
    """Model definition for Diplome."""

    # TODO: Define fields here
    nom_diplome         = models.CharField( max_length=50)
    fichier =     models.ForeignKey(DossierRecrutement, on_delete=models.CASCADE, related_name="diplome")
    document            = models.FileField(upload_to ='recrutement/diplomes/',default='none.png',validators=[validate_file_extension_for_document]) 
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Diplome."""

        verbose_name = 'Diplome'
        verbose_name_plural = 'Diplomes'

    def __str__(self):
        """Unicode representation of Diplome."""
        return self.nom_diplome

    def get_absolute_url(self):
        """Return absolute url for Diplome."""
        return ('')

    # TODO: Define custom methods here

####################################################################################################################################################
####################################################################################################################################################

class Certificat(models.Model):
    """Model definition for Certificat."""

    # TODO: Define fields here
    nom_certificat        = models.CharField( max_length=50)
    documents =      models.ForeignKey(DossierRecrutement, on_delete=models.CASCADE, related_name="certificat")
    fichier            = models.FileField(upload_to ='recrutement/certificats/',default='none.png',validators=[validate_file_extension_for_document]) 
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Certificat."""

        verbose_name = 'Certificat'
        verbose_name_plural = 'Certificats'

    def __str__(self):
        """Unicode representation of Certificat."""
        return self.nom_certificat


    def get_absolute_url(self):
        """Return absolute url for Certificat."""
        return ('')

    # TODO: Define custom methods here

#######################################################################################################################################################
#######################################################################################################################################################

class Jury(models.Model):
    """Model definition for Jury."""

    # TODO: Define fields here
    recrutement         = models.ForeignKey('Recrutement', models.DO_NOTHING)
    membre =  models.ManyToManyField(Enseignant, related_name="membrejury")
    dossier =  models.ManyToManyField(DossierRecrutement, related_name="dossierjury")
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Jury."""

        verbose_name = 'Jury'
        verbose_name_plural = 'Jurys'

    def __str__(self):
        """Unicode representation of Jury."""
        return self.recrutement.intitule


    def get_absolute_url(self):
        """Return absolute url for Recrutement."""
        return (reverse("accueil-teacher", kwargs={"pk": self.pk})) # 


    # TODO: Define custom methods here


#######################################################################################################################################################
class ResultatSet(QuerySet, GroupByMixin):
    pass
#######################################################################################################################################################

class Resultat(models.Model):
    """Model definition for Resultat."""
    objects = ResultatSet.as_manager()
    # TODO: Define fields here
    dossier = models.ForeignKey(DossierRecrutement, on_delete=models.CASCADE,)
    juge = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    critere1 = models.IntegerField()
    critere2 = models.IntegerField()
    critere3 = models.IntegerField()
    critere4 = models.IntegerField()
    critere5 = models.IntegerField()
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Resultat."""

        verbose_name = 'Resultat'
        verbose_name_plural = 'Resultats'
       

    def __str__(self):
        """Unicode representation of Resultat."""
        return "{} {}".format(self.dossier.nom, self.dossier.prenom)


    def get_absolute_url(self):
        """Return absolute url for Resultat."""
        return ('')

    @property
    def Moyenne(self):
        total = self.critere1 + self.critere2 +self.critere3 +self.critere4 +self.critere5 
        moy = total /5
        return moy
    @property
    def All(self):
       all_resultat = Resultat.objects.filter(dossier=self.dossier)
       som  = 0 
       for i in all_resultat:
           som = som + i.Moyenne
       Moyenne_final = som/all_resultat.count()
       return  round(Moyenne_final,2)


    # TODO: Define custom methods here
########################################################################################################################################################
########################################################################################################################################################

