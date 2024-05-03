from django.db import models

class PuneJobs(models.Model):
    date = models.DateField()
    company_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    skills_required = models.CharField(max_length=30)
    experience = models.IntegerField()
    city = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.BigIntegerField()

class BangloreJobs(models.Model):
    date = models.DateField()
    company_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    skills_required = models.CharField(max_length=30)
    experience = models.IntegerField()
    city = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.BigIntegerField()

class ChennaiJobs(models.Model):
    date = models.DateField()
    company_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    skills_required = models.CharField(max_length=30)
    experience = models.IntegerField()
    city = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.BigIntegerField()

class MumbaiJobs(models.Model):
    date = models.DateField()
    company_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    skills_required = models.CharField(max_length=30)
    experience = models.IntegerField()
    city = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
