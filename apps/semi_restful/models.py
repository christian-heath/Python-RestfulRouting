from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if postData["first_name"].isalpha() != True:
            errors['first_name'] = "Invalid first name."
        if postData["last_name"].isalpha() != True:
            errors['last_name'] = "Invalid last name."  
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email."
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)    
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()