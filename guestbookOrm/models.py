from django.db import models

class Guestbook(models.Model):
    name =models.CharField(max_length=45)
    password =models.CharField(max_length=45)
    message =models.TextField
    regdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Guestbook({self.name},{self.password},{self.message},{self.regdate})'
