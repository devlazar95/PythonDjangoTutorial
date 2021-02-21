from django.db import models
import uuid


class Employee(models.Model):
    GENDER_CHOICE = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    middle_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICE, default="m")
    address = models.CharField(max_length=255, default='')
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=False, null=False)


class Sector(models.Model):
    sector_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)


class Project(models.Model):
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    employees = models.ManyToManyField(Employee)
