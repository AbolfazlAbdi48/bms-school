from django.db import models


# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام سنسور')
    description = models.CharField(max_length=255, verbose_name='جزئیات سنسور')
    quantity = models.CharField(max_length=100, default="درجه", verbose_name='واحد')

    def __str__(self):
        return self.name


class SensorDetail(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='سنسور')
    value = models.CharField(max_length=100, verbose_name='مقدار')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.sensor} - {self.value}"


class Lamp(models.Model):
    STATUS_CHOICES = (
        ("0", "OFF"),
        ("1", "ON")
    )
    name = models.CharField(max_length=255, verbose_name='نام لامپ')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='0', verbose_name='وضعیت')

    def __str__(self):
        return f"{self.name} - {self.status}"
