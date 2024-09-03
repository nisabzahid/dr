from django.db import models

# Create your models here.


class Cars(models.Model):
    owner_name = models.CharField("Owner Name", max_length=240)
    email = models.EmailField()
    document = models.CharField("Document", max_length=20)
    number = models.CharField(max_length=20)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.owner_name
