from django.db import models
import json


class Resume(models.Model):
    select_category = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    current_location = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    highest_qualification = models.CharField(max_length=255, null=True, blank=True)
    experience = models.CharField(max_length=255, null=True, blank=True)
    currnet_ctc = models.CharField(max_length=255, null=True, blank=True)
    expected_ctc = models.CharField(max_length=255, null=True, blank=True)
    working_status = models.CharField(max_length=255, null=True, blank=True)
    notice_period = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    follow_status = models.CharField(max_length=20, null=True, blank=True)
    selection_status = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    checkbox_values = models.BooleanField(null=True, blank=True)
    key_skill = models.CharField(max_length=255, null=True, blank=True)
    skill = models.CharField(max_length=255, null=True, blank=True)
    my_file = models.FileField(upload_to="uploads/", null=True, blank=True)
    remark = models.TextField(null=True, blank=True)
