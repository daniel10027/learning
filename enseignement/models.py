from django.db import models
from tinymce import HTMLField
from gestion.validators import validate_file_extension_for_image,validate_file_extension_for_document


# Create your models here.
###########################################################
class Localite(models.Model):
    """Model definition for Localite."""

    # TODO: Define fields here
    nom         = models.CharField( max_length=50)
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Localite."""

        verbose_name = 'Localite'
        verbose_name_plural = '              Localites'

    def __str__(self):
        """Unicode representation of Localite."""
        return self.nom

    

    def get_absolute_url(self):
        """Return absolute url for Localite."""
        return ('')

    # TODO: Define custom methods here
#######################################################
class TypeEtablissement(models.Model):
    """Model definition for TypeEtablissement."""

    # TODO: Define fields here
    nom         = models.CharField( max_length=50, help_text="Exemple: Universite / Grande Ecole")
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for TypeEtablissement."""

        verbose_name = 'TypeEtablissement'
        verbose_name_plural = '             TypeEtablissements'

    def __str__(self):
        """Unicode representation of TypeEtablissement."""
        return self.nom

    

    def get_absolute_url(self):
        """Return absolute url for TypeEtablissement."""
        return ('')

    # TODO: Define custom methods here
###########################################################
class StatutEtablissement(models.Model):
    """Model definition for StatutEtablissement."""

    # TODO: Define fields here
    nom         = models.CharField( max_length=50, help_text="Exemple: Public /Prive")
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for StatutEtablissement."""

        verbose_name = 'StatutEtablissement'
        verbose_name_plural = '            StatutEtablissements'

    def __str__(self):
        """Unicode representation of StatutEtablissement."""
        return self.nom

    
    def get_absolute_url(self):
        """Return absolute url for StatutEtablissement."""
        return ('')

    # TODO: Define custom methods here
##########################################################
class Etablissement(models.Model):
    """Model definition for Etablissement."""

    # TODO: Define fields here
    nom  = models.CharField( max_length=50, help_text="Nom de l'etablissement")
    localite = models.ForeignKey(Localite,on_delete=models.CASCADE)
    adresse  = models.CharField(max_length=50)
    type_etablissement = models.ForeignKey(TypeEtablissement, on_delete=models.CASCADE)
    statut_etablissement = models.ForeignKey(StatutEtablissement, on_delete=models.CASCADE)
    directeur_general =  models.CharField(max_length=50, help_text="nom et prenom du Directeur General")
    email = models.EmailField(blank=True)
    contact = models.CharField(max_length=8)
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)   

    class Meta:
        """Meta definition for Etablissement."""

        verbose_name = 'Etablissement'
        verbose_name_plural = '           Etablissements'

    def __str__(self):
        """Unicode representation of Etablissement."""
        return "{}({})".format(self.nom, self.localite.nom)

    

    def get_absolute_url(self):
        """Return absolute url for Etablissement."""
        return ('')

    # TODO: Define custom methods here
##########################################################
class DominaceUfr(models.Model):
    """Model definition for DominaceUfr."""

    # TODO: Define fields here
    nom         = models.CharField( max_length=50, help_text="Exemple: Mathematique/Physique/Literaire")
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for DominaceUfr."""

        verbose_name = 'DominaceUfr'
        verbose_name_plural = '          DominaceUfrs'

    def __str__(self):
        """Unicode representation of DominaceUfr."""
        return self.nom

    

    def get_absolute_url(self):
        """Return absolute url for DominaceUfr."""
        return ('')

    # TODO: Define custom methods here
###############################################################
class Ufr(models.Model):
    """Model definition for Ufr."""

    # TODO: Define fields here

    nom         = models.CharField( max_length=50)
    dominace = models.ForeignKey(DominaceUfr, on_delete=models.CASCADE)
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE , related_name="etablissement_ufr")
    situation = HTMLField('situation Geographique')
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Ufr."""

        verbose_name = 'Ufr'
        verbose_name_plural = '         Ufrs'

    def __str__(self):
        """Unicode representation of Ufr."""
        return "{} ({})".format(self.nom, self.etablissement.nom)


    def get_absolute_url(self):
        """Return absolute url for Ufr."""
        return ('')

    # TODO: Define custom methods here

    ###############################################################
class Filiere(models.Model):
        """Model definition for Filiere."""
    
        # TODO: Define fields here
        nom         = models.CharField( max_length=50)
        departement = models.ForeignKey(Ufr, on_delete=models.CASCADE)
        status      = models.BooleanField(default=True)
        created     = models.DateTimeField(auto_now_add=True)
        date_update = models.DateTimeField(auto_now=True)
    
        class Meta:
            """Meta definition for Filiere."""
    
            verbose_name = 'Filiere'
            verbose_name_plural = '        Filieres'
    
        def __str__(self):
            """Unicode representation of Filiere."""
            return "{} {}({})".format(self.nom, self.departement.nom, self.departement.etablissement.nom)
    
        
    
        def get_absolute_url(self):
            """Return absolute url for Filiere."""
            return ('')
    
        # TODO: Define custom methods here
    

############################################################################
class Specialite(models.Model):
    """Model definition for Specialite."""

    # TODO: Define fields here
    nom         = models.CharField( max_length=50)
    filiere = models.ForeignKey(Filiere,on_delete=models.CASCADE, related_name="specialite_filiere")
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Specialite."""

        verbose_name = 'Specialite'
        verbose_name_plural = '       Specialites'

    def __str__(self):
        """Unicode representation of Specialite."""
        return "SPECIALITÉ:{} | FILIERE: {} | UFR: {} | ETABLISSEMNT: ({})".format(self.nom, self.filiere.nom, self.filiere.departement.nom, self.filiere.departement.etablissement.nom)

   

    def get_absolute_url(self):
        """Return absolute url for Specialite."""
        return ('')

    # TODO: Define custom methods here


################################################################################
class Niveau(models.Model):
    """Model definition for NIveau."""

    # TODO: Define fields here

    nom         = models.CharField( max_length=50, help_text="Exemple: Licence/Master...")
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for NIveau."""

        verbose_name = 'Niveau'
        verbose_name_plural = '      Niveaux'

    def __str__(self):
        """Unicode representation of Niveau."""
        return self.nom

    

    def get_absolute_url(self):
        """Return absolute url for NIveau."""
        return ('')

    # TODO: Define custom methods here
##############################################################
class Semestre(models.Model):
    """Model definition for Semestre."""

    # TODO: Define fields here

    nom         = models.CharField( max_length=50, help_text="Exemple: Semestre 1")
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Semestre."""

        verbose_name = 'Semestre'
        verbose_name_plural = '     Semestres'

    def __str__(self):
        """Unicode representation of Semestre."""
        return self.nom

    

    def get_absolute_url(self):
        """Return absolute url for Semestre."""
        return ('')

    # TODO: Define custom methods here
#####################################################################
class TypeUe(models.Model):
    """Model definition for TypeUe."""

    # TODO: Define fields here
    nom         = models.CharField( max_length=50, help_text="Exemple: Conaaissance Fondementale/Culture Generale")
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for TypeUe."""

        verbose_name = 'TypeUe'
        verbose_name_plural = '    TypeUes'

    def __str__(self):
        """Unicode representation of TypeUe."""
        return self.nom

    
    def get_absolute_url(self):
        """Return absolute url for TypeUe."""
        return ('')

    # TODO: Define custom methods here
####################################################################
class UniteEnseignement(models.Model):
    """Model definition for UniteEnseignement."""

    # TODO: Define fields here
    nom         = models.CharField( max_length=50)
    type = models.ForeignKey(TypeUe, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE)
    objectif_general = HTMLField('objectif_general')
    objectif_specifique =HTMLField('objectif specifique')
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for UniteEnseignement."""

        verbose_name = 'UniteEnseignement'
        verbose_name_plural = '   UniteEnseignements'

    def __str__(self):
        """Unicode representation of UniteEnseignement."""
        return "{} {}".format(self.nom, self.specialite.nom, self.specialite.filiere.departement.etablissement.nom)

   

    def get_absolute_url(self):
        """Return absolute url for UniteEnseignement."""
        return ('')

    # TODO: Define custom methods here
#####################################################################################################################
class Ecue(models.Model):
    """Model definition for Ecue."""

    # TODO: Define fields here
    intitule = models.CharField(max_length=50)
    image = models.ImageField(upload_to='enseignement/ecue',default='none.png')
    objectif_general = HTMLField('objectif_general')
    objectif_specifique =HTMLField('objectif specifique')
    enseignant = models.ForeignKey('gestion.Enseignant', on_delete=models.CASCADE, related_name="ecue_enseignant")
    ue = models.ForeignKey(UniteEnseignement, on_delete=models.CASCADE,related_name="ecue_ue")
    competence = HTMLField('Competences visées')
    materiel = HTMLField('Materiel pédagogique')
    temp_cours_magistral  =  models.IntegerField()
    temps_travaux_dirige=  models.IntegerField()
    temps_travaux_pratique  =  models.IntegerField()
    credit  =  models.IntegerField()
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


    class Meta:
        """Meta definition for Ecue."""

        verbose_name = 'Ecue'
        verbose_name_plural = ' Ecue'

    def __str__(self):
        """Unicode representation of Ecue."""
        return "{} |UE: {} | SPECIALITE: {} | ETABLISSEMENT: {}".format(self.intitule, self.ue.nom, self.ue.specialite.nom,self.ue.specialite.filiere.departement.etablissement.nom)

    
    def get_absolute_url(self):
        """Return absolute url for Ecue."""
        return reverse("course-list", kwargs={"pk": self.pk}) # 
    # TODO: Define custom methods here
###########################################################################
###########################################################################
class Cours(models.Model):
    """Model definition for Cours."""

    # TODO: Define fields here
    ecue = models.ForeignKey(Ecue, on_delete=models.CASCADE)
    intitule = models.CharField(max_length=50)
    image = models.ImageField(upload_to='enseignement/cours',default='none.png',validators=[validate_file_extension_for_image])
    prerequis =  HTMLField('Pre_requis')
    competence = HTMLField('Competences visées')
    consigne = HTMLField('Consigne')
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)   

    class Meta:
        """Meta definition for Cours."""

        verbose_name = 'Cours'
        verbose_name_plural = 'Cours'

    def __str__(self):
        """Unicode representation of Cours."""
        return self.intitule

    

    def get_absolute_url(self):
        """Return absolute url for Cours."""
        return reverse("course-detail", kwargs={"pk": self.pk}) # rediriger apres creation de produuits

    # TODO: Define custom methods here
##################################################################
class RessourcePdf(models.Model):
    """Model definition for RessourcePdf."""

    # TODO: Define fields here
    cours        = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name="ressourcepdf")
    nom = models.CharField( max_length=50)
    fichier = models.FileField(upload_to ='cours/pdf/% Y/% m/% d/',default='none.png') 
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for RessourcePdf."""

        verbose_name = 'RessourcePdf'
        verbose_name_plural = 'RessourcePdfs'

    def __str__(self):
        """Unicode representation of RessourcePdf."""
        return self.cours.intitule

    

    def get_absolute_url(self):
        """Return absolute url for RessourcePdf."""
        return ('')

    # TODO: Define custom methods here
########################################################################
class RessourceVideo(models.Model):
    """Model definition for RessourceVideo."""

    # TODO: Define fields here
    nom = models.CharField( max_length=50)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name="ressourcevideo")
    url = models.URLField(max_length = 200) 
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for RessourceVideo."""

        verbose_name = 'RessourceVideo'
        verbose_name_plural = ','

    def __str__(self):
        """Unicode representation of RessourceVideo."""
        return self.cours.intitule

    def get_absolute_url(self):
        """Return absolute url for RessourceVideo."""
        return ('')

    # TODO: Define custom methods here
