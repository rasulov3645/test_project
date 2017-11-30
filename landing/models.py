from django.db import models

# Create your models here.

class Subcriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.email,)
        # return self.name

    class Meta:
        verbose_name = "MySubcriber"
        verbose_name_plural = "A lot of Subcribers"
