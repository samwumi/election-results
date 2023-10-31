from django.db import models

class States(models.Model):
    id = models.IntegerField()
    party_id = models.IntegerField(primary_key=True)
    partyname = models.CharField(max_length=100)

class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    ward = models.ForeignKey('Ward', on_delete=models.CASCADE)
    lga = models.ForeignKey('LGA', on_delete=models.CASCADE)
    state = models.ForeignKey('States', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Ward(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    lga = models.ForeignKey('LGA', on_delete=models.CASCADE)

class LGA(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    lga_name = models.CharField(max_length=100)
    lga_id = models.IntegerField(default=0)
    state_id = models.ForeignKey('States', on_delete=models.CASCADE)
    lga_description = models.CharField(max_length=1000)
    entered_by_user = models.CharField(max_length=200, default= 'Adewumi')
    date_entered = models.DateTimeField(default=None, null=True, blank=True)
    user_ip_address = models.GenericIPAddressField(default='0.0.0.0')



class States(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=100)

class AnnouncedPuResults(models.Model):
    result_id = models.IntegerField()
    polling_unit = models.ForeignKey('PollingUnit', on_delete=models.CASCADE)
    party_abbreviation = models.CharField(max_length=100)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=200, default= 'Adewumi')
    date_entered = models.DateTimeField(default=None, null=True, blank=True)
    user_ip_address = models.GenericIPAddressField(default='0.0.0.0')

class AnnouncedLgaResults(models.Model):
    result_id = models.IntegerField(default=100)
    lga_name =   models.IntegerField(default=0)
    party_abbreviation = models.CharField(max_length=100, default='PDP')
    party_score = models.IntegerField(default=200)
    entered_by_user = models.CharField(max_length=200, default= 'Adewumi')
    date_entered = models.DateTimeField(default=None, null=True, blank=True)
    user_ip_address = models.GenericIPAddressField(default='0.0.0.0')
