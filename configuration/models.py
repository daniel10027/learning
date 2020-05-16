from django.db import models
from PIL import Image
from gestion.validators import validate_file_extension_for_image,validate_file_extension_for_document

# Create your models here.
##########################################################################################
class Partenaire(models.Model):
    """Model definition for Partenaire."""
    nom         = models.CharField( max_length=50)
    logo        = models.FileField(upload_to ='partenaires/logo',default='none.png',validators=[validate_file_extension_for_image])
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Partenaire."""

        verbose_name = 'Partenaire'
        verbose_name_plural = 'Partenaires'

    def __str__(self):
        """Unicode representation of Partenaire."""
        return self.nom

    
    def get_absolute_url(self):
        """Return absolute url for Partenaire."""
        return ('')

    # TODO: Define custom methods here


class CopyRight(models.Model):
    """Model definition for CopyRight."""
    nom         = models.CharField( max_length=50)
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for CopyRight."""

        verbose_name = 'CopyRight'
        verbose_name_plural = 'CopyRights'

    def __str__(self):
        """Unicode representation of CopyRight."""
        return self.nom


class ContactInfo(models.Model):
    """Model definition for ContactInfo."""
    titre        = models.CharField( max_length=50)
    description  = models.TextField()
    adresse = models.CharField( max_length=50)
    pays = models.CharField( max_length=50)
    contact1 = models.CharField( max_length=8)
    contact2 = models.CharField( max_length=8)
    email = models.EmailField( max_length=254)
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for ContactInfo."""

        verbose_name = 'ContactInfo'
        verbose_name_plural = 'ContactInfos'

    def __str__(self):
        """Unicode representation of ContactInfo."""
        return self.titre

############################MESSAGE##############################
class Message(models.Model):
    """Model definition for Message."""
    titre        = models.CharField( max_length=50)
    description  = models.TextField()
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Message."""

        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['-created']

    def __str__(self):
        """Unicode representation of Message."""
        return self.titre

   

    def get_absolute_url(self):
        """Return absolute url for Message."""
        return ('')

    # TODO: Define custom methods here