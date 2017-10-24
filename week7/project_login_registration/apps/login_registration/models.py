# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Create your models here.

class UserManager(models.Manager):

    def validate_login(self, postData):
        errors=[]
        #This checks the DB for a match to postData['email']
        if len(self.filter(email=postData['email'])) > 0:
            #This checks the DB for a match to postData['password']
            user = self.filter(email=postData['email'])[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors.append('Email or password is incorrect.')

        else:
            errors.append('Email or password is incorrect.')

        if errors:
            return errors

        return user

    def validate_registration(self, postData):
        errors =[]
        #loop through dict to make sure there are no empty fields, if so closes
        for key, value in postData.iteritems():
            if len(value) < 1:
                errors.append("Please fill out all of the required fields.")
                break
        #This checks the length of first and last name
        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
            errors.append("Please fill out your first and last name.")
        #Checks for numbers and special characters in the name fields
        if not re.match(NAME_REGEX, postData['first_name']) or not re.match(NAME_REGEX, postData['last_name']):
            errors.append('Your first and last name can not contain special charaters or numbers.')
        #Checks to make sure the email is valid
        if not re.match(EMAIL_REGEX, postData['email']):
            errors.append('Please enter a valid email address.')
        #This makes sure the password is 8 characters in length
        if len(postData['password']) < 8:
            errors.append("Your password must be at least 8 characters in length.")
        #This checks the two passwords given
        if len(postData['password']) != len(postData['confpassword']):
            errors.append('Your password and password confirmation do not match.')
        #If no errors happen, this creates a new user.
        if not errors:
            hashed=bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt(5))
            new_user = self.create(
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                email=postData['email'],
                password=hashed
            )
            return new_user

        return errors
    
class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
