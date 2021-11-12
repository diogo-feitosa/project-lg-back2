from django.db import models

# Create your models here.
class Project(models.Model):

    RiskEnum = (
       (0,'low'),		
	   (1,'medium'), 			
	   (2,'high')
    )

    name = models.CharField(max_length=30)

    startDate = models.DateField(max_length=30)

    endDate = models.DateField(max_length=30)

    value = models.FloatField(max_length=30)

    risk = models.IntegerField(max_length=1, choices=RiskEnum, blank=False, null=False)

    def __str__(self):
        return self.name