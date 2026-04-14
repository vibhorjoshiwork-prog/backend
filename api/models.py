from django.db import models

# Location Model
class Location(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.latitude}, {self.longitude})"


# Safety Report Model
class SafetyReport(models.Model):
    REPORT_CHOICES = [
        ('POLICE_PATROL', 'Police Patrol'),
        ('STREET_LIGHT', 'Street Light'),

        ('HARASSMENT', 'Harassment'),
        ('NO_CROWD', 'No Crowd'),

        ('THEFT', 'Theft'),
        ('FIGHT', 'Fight'),
        ('CONFLICT', 'Conflict'),
        ('RIOT', 'Riot'),
    ]

    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='reports')
    report_type = models.CharField(max_length=20, choices=REPORT_CHOICES)  # 🔥 increased length
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    severity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.location.name} - {self.report_type}"