from django.db import models

# Create your models here.

class Note(models.Model):
    note_name = models.CharField(max_length=15)
    note_desc = models.CharField(max_length=200)
    note_status = models.BooleanField('note status') #set boolean value when creating note -> set to false
    note_date_created = models.DateTimeField('date created')

    def __str__(self):
        return self.note_name