# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate_course(self,postData):
        errors =[]
        #loop through dict to make sure there are no empty fields, if so closes
        for key, value in postData.iteritems():
            if len(value) < 1:
                errors.append("Please fill out the course name and descripition")
                break
        #This checks the length of course name and course desc
        if len(postData['name']) < 5 or len(postData['desc']) < 15:
            errors.append("The course name must be five characters in length and the course description must be fifteen characters in length.")

        return errors


class Course(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CourseManager()