#coding:utf-8

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
	photo     =  models.ImageField(upload_to='photo',blank=True)
	descript  =  models.TextField()
	user      =  models.ForeignKey(User)
	
class Student(models.Model):
	photo     =  models.ImageField(upload_to='photo',blank=True)
	descript  =  models.TextField()
	user      =  models.ForeignKey(User)
	level     =  models.CharField(max_length=64)	
 
class Question(models.Model):
	content = models.CharField(max_length=1024)
	result  = models.CharField(max_length=256)
	teacher = models.ForeignKey(Teacher)
	tested  = models.IntegerField(default=0,verbose_name='已测试人数')
        bingo   = models.IntegerField(default=0,verbose_name='正确的人数')
	times   = models.IntegerField(default=0,verbose_name='总耗时')
	level   = models.CharField(max_length=64)	

class QuestionInfo(models.Model):
	studentid   = models.IntegerField()
	questionid  = models.IntegerField()
	start_time  = models.DateTimeField()
	end_time    = models.DateTimeField()
	times       = models.IntegerField()
	bingo       = models.IntegerField()
	status      = models.IntegerField(default=0)
	result      = models.CharField(max_length=256)
	

