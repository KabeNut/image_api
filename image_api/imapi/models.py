from django.db import models

# Create your models here.
def user_dir_path(instance, filename):
    return 'images/{0}/'.format(filename)

class Images(models.Model):
    uid = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to=user_dir_path
    )