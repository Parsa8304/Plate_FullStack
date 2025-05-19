from django.db import models


class Plate(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=255)
    plate_number = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.image_name}: {self.plate_number}"

   
