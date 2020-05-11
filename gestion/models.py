from django.db import models
from django.conf import settings
from django.utils import timezone
from enseignement.models import Localite, Etablissement, Specialite, Niveau
from django.utils.html import escape, mark_safe
from django.contrib.auth.models import AbstractUser

#####################VALIDATOR####################################
from django.core.exceptions import ValidationError

def validate_file_extension_for_document(value):
  import os
  ext = os.path.splitext(value.name)[1]
  size = value.size
  valid_extensions = ['.pdf']
  if not ext in valid_extensions:
    raise ValidationError(u'Les dossiers doivent etre au format PDF ')
  if size > 838856 :
      raise ValidationError("La Taille maximale de chaque fichier est 500Ko .")
  else:
      return value

def validate_file_extension_for_image(value):
  import os
  ext = os.path.splitext(value.name)[1]
  size = value.size
  valid_extensions = ['.png','.jpeg','.jpg']
  if not ext in valid_extensions:
    raise ValidationError(u'Les dossiers doivent etre au format Image (PNG, JPEG, JPG)')
  if size > 838856 :
      raise ValidationError("La Taille maximale de chaque fichier est 500Ko .")
  else:
      return value



#########################################################

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

    def __str__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.username)

#########################################################
class Grade(models.Model):
    """Model definition for Grade."""

    # TODO: Define fields here
    nom         = models.CharField( max_length=50)
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Grade."""

        verbose_name = 'Grade'
        verbose_name_plural = '    Grades'

    def __str__(self):
        """Unicode representation of Grade."""
        return self.nom
###################################################################

class TypeEnseignant(models.Model):
    """Model definition for TypeEnseignant."""

    # TODO: Define fields here
    nom         = models.CharField( max_length=50)
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for TypeEnseignant."""

        verbose_name = 'TypeEnseignant'
        verbose_name_plural = 'TypeEnseignants'

    def __str__(self):
        """Unicode representation of TypeEnseignant."""
        return self.nom


##################################################################
class Domaine(models.Model):
    """Model definition for DomaineCompetence."""

    # TODO: Define fields here
    nom         = models.CharField( max_length=50)
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for DomaineCompetence."""

        verbose_name = 'Domaine'
        verbose_name_plural = '   Domaines'

    def __str__(self):
        """Unicode representation of DomaineCompetence."""
        return self.nom

##################################################################
class Student(models.Model):
   
    # TODO: Define fields here
    sexe_choice =  (
        ('H', 'Homme',),
        ('F', 'Femme',),
    )
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    etablissemnt = models.ForeignKey(Etablissement,blank=True, null=True,on_delete=models.CASCADE)
    specialite = models.ForeignKey(Specialite,blank=True, null=True, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau,blank=True, null=True, on_delete=models.CASCADE)
    date_de_naissance = models.DateField(default=timezone.now)
    localite = models.ForeignKey(Localite, on_delete=models.CASCADE,blank=True, null=True)
    sexe =  models.CharField( max_length=1,choices=sexe_choice,)
    contact = models.CharField(max_length=8) 
    piece_indentite   = models.FileField(upload_to ='student/piece',default='none.png',validators=[validate_file_extension_for_document]) 
    photo             = models.FileField(upload_to ='studentphotos/',default='none.png',validators=[validate_file_extension_for_image]) 
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define custom methods here

    class Meta:
        """Meta definition for Student."""

        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        """Unicode representation of Student."""
        return self.user.username

    def get_absolute_url(self):
        """Return absolute url for Student."""
        return ('')

    # TODO: Define custom methods here
#########################################################################
#########################################################################

class Enseignant(models.Model):
    """Model definition for Enseignant."""

    # TODO: Define fields here
    sexe_choice =  (
        ('H', 'Homme',),
        ('F', 'Femme',),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricule  = models.CharField( max_length=20)
    type = models.ForeignKey(TypeEnseignant, on_delete=models.CASCADE,blank=True, null=True)
    structure  = models.CharField( max_length=50, help_text="structure d'enseignement")
    date_de_naissance = models.DateField(default=timezone.now)
    localite = models.ForeignKey(Localite, on_delete=models.CASCADE,blank=True, null=True)
    sexe =  models.CharField( max_length=1,choices=sexe_choice,)
    contact = models.CharField(max_length=8)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True, null=True)
    domaine = models.ManyToManyField(Domaine, related_name="competence_enseignant")
    piece_indentite   = models.FileField(upload_to ='enseignant/pieces/',default='none.png',validators=[validate_file_extension_for_document]) 
    photo             = models.FileField(upload_to ='enseignant/photos/',default='none.png',validators=[validate_file_extension_for_image]) 
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


    class Meta:
        """Meta definition for Enseignant."""

        verbose_name = 'Enseignant'
        verbose_name_plural = 'Enseignants'

    def __str__(self):
        """Unicode representation of Enseignant."""
        return "{} {}".format(self.user.first_name,self.user.last_name)
    

    def get_absolute_url(self):
        """Return absolute url for Enseignant."""
        return ('')

    # TODO: Define custom methods here

#################################################################################
class Tuteur(models.Model):
    """Model definition for Tuteur."""

    # TODO: Define fields here
    sexe_choice =  (
        ('H', 'Homme',),
        ('F', 'Femme',),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    structure  = models.CharField( max_length=50, help_text="structure d'enseignement")
    date_de_naissance = models.DateField(default=timezone.now)
    localite = models.ForeignKey(Localite, on_delete=models.CASCADE,blank=True, null=True)
    sexe =  models.CharField( max_length=1,choices=sexe_choice,)
    contact = models.CharField(max_length=8)
    domaine = models.ManyToManyField(Domaine, related_name="competence_tuteur")
    piece_indentite   = models.FileField(upload_to ='tuteurs/pieces/',default='none.png',validators=[validate_file_extension_for_document]) 
    photo             = models.FileField(upload_to ='tuteurs/photos/',default='none.png',validators=[validate_file_extension_for_image]) 
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Tuteur."""

        verbose_name = 'Tuteur'
        verbose_name_plural = 'Tuteurs'

    def __str__(self):
        """Unicode representation of Tuteur."""
        return self.user.username

    

    def get_absolute_url(self):
        """Return absolute url for Tuteur."""
        return ('')

    # TODO: Define custom methods here
