# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
'''
    first_name 255
    last_name 255
    email_address 255
    age int
    created_at
    updated_at

    Please do the following

    Create a new model called 'User' with the information above.
    Successfully create and run the migration files
    Using the shell...
    Know how to retrieve all users.
    Know how to get the last user.
    Create a few records in the users
    Know how to get the first user.
    Know how to get the users sorted by their first name (order by first_name DESC)
    Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. Know how to do this directly in the console using .get and .save.
    Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...).
    (optional) Ninja:
    Find a way to validate the data coming in to the shell.  
    For example, make sure that "name" fields are a minimum length, "email" is a valid email, or that "email" doesn't already exist in the db.
'''

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)