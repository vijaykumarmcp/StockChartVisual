from django.db import models
from django.conf import settings

# Create your models here.
class Note(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    url=models.URLField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_delete_url(self):
        return "/notes/{}/delete".format(self.pk)

    def get_update_url(self):
        return "/notes/{}/update".format(self.pk)

