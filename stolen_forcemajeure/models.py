from django.db import models

class Sites(models.Model):
    ne_state = models.CharField(max_length=6, null=True)
    site_id = models.CharField(max_length=8)
    site_name = models.CharField(max_length=100)
    area = models.CharField(max_length=20, null=True)
    region = models.CharField(max_length=30, null=True)
    micro_cluster = models.CharField(max_length=40, null=True)
    
    def __str__(self):
        return self.site_id

class Cases(models.Model):
    pass