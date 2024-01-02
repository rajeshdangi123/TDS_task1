from django.db import models
from django.db.models import Q


# Create your models here.
from djongo import models


class SaleEnquiry(models.Model):
    client_name = models.CharField(max_length=255, blank=True, null=True)
    guardian_type = models.CharField(max_length=10, blank=True, null=True)
    guardian_name = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField()
    mobile_no = models.CharField(max_length=10, blank=True, null=True)
    additional_mobile_no = models.CharField(max_length=10, blank=True)
    address = models.TextField()
    state = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    next_follow_up_date = models.DateField()
    notes = models.TextField()
    record_updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name

    def isExists(self):
        if SaleEnquiry.objects.filter(
            Q(mobile_no=self.mobile_no)
            | Q(additional_mobile_no=self.additional_mobile_no)
        ):
            return True
        else:
            return False

    def register(self):
        self.save()
