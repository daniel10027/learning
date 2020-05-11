
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
    raise ValidationError(u"L'image doit etre au format Image (PNG, JPEG, JPG)")
  if size > 838856 :
      raise ValidationError("La Taille maximale de chaque fichier est 500Ko .")
  else:
      return value