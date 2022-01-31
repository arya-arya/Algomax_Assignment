from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    date = models.DateField(_("Date"), default=datetime.date.today)
    income = models.CharField(max_length=100)
    IP address =models.DateField()