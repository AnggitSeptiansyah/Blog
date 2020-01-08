from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    """ 
        *** FUNGSI CASCADE ***

        Cascade adalah sebuah cara untuk menghapus.
        jika user dihapus maka profile juga akan terhapus,
        dan jika profile dihapus maka cuma profile saja yang dihapus,
        sedangkan yang lainnya tidak
    """
    user        = models.OneToOneField(User, on_delete = models.CASCADE)
    image       = models.ImageField(default = 'default.png', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


