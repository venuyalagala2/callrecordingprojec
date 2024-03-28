from django.db import models

# Create your models here.
class CallRecord(models.Model):
    caller_id = models.IntegerField()
    caller_name = models.CharField(max_length=100)
    caller_phone_number = models.CharField(max_length=12)
    caller_location = models.CharField(max_length =100)
    caller_organization = models.CharField(max_length =100)
    caller_job_title =models.CharField(max_length =100)
    receiver_name = models.CharField(max_length =100)
    receiver_phone_number = models.CharField(max_length =12)
    receive_location = models.CharField(max_length =100)
    receiver_organization = models.CharField(max_length =100)
    receiver_job_title = models.CharField(max_length =100)
    notes = models.CharField(max_length =200)
    quality_rating = models.FloatField()
    duration_seconds= models.DurationField()
    recording_url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caller_name
