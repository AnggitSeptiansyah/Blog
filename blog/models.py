from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

""" Migration Command

1. Mengeksekusi Migrate                     --> python manage.py migrate
2. Membuat Migrasi Database                 --> python manage.py makemigration
3. Cara melihat Model dalam bentuk Database --> python manage.py sqlmigrate blog 001 (001 merupakan nama file yang berada pada migrations->001initial)

Note :
    ** Untuk membuat migrasi maka terlebih dahulu membuat class pada models


"""

class Post(models.Model):
    title       = models.CharField(max_length = 100)
    content     = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author      = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    




