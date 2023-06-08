from django.db import models


class Data(models.Model):# model will save the data into the database
    picture = models.ImageField(upload_to='media/data_pictures/')
    node_origination = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    file_type = models.CharField(max_length=50)

    def __str__(self):
        return f"Data ID: {self.pk}"
