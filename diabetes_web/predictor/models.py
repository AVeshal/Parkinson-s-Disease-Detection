from django.db import models

class Prediction(models.Model):
    pregnancies = models.FloatField()
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    dpf = models.FloatField()
    age = models.FloatField()
    result = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.result} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
