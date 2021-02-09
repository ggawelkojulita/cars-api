from django.db import models


class Car(models.Model):
    make_name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('make_name', 'model_name',)


class Rate(models.Model):
    CHOICES = [(i, i) for i in range(1, 6)]

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    value = models.IntegerField(choices=CHOICES)
