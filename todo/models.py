from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
from django.utils import timezone
from django.db.models import Avg, Count, Min, Sum
# Create your models here.

Status =(
    ("I Take from Him", "I Take from Him"),
    ("I Gave to Him", "I Gave to Him"),
    ("Pending On Me" , "Pending On Me" ),
    ("Pending On Him" , "Pending On Him" )
    
)


Mode =(
    ("Cash", "Cash"),
    ("Bank Transfer", "Bank Transfer"),
    ("Online", "Online"),     
)


class WeekProject(models.Model):
    job = models.CharField(max_length = 500)
    job_descriptions = models.TextField()
    initiate = models.BooleanField(default=False)
    halfway = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    weekproject_highlight = models.CharField( max_length = 1000 , null = True , blank = True)
    published = models.DateTimeField(auto_now_add = True)
    author 		= models.ForeignKey(User, on_delete= models.CASCADE)


    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.job


class Task(models.Model):
	taskname = models.CharField(max_length = 500)
	task_descriptions = models.TextField() #remove null when go to deploy
	published = models.DateTimeField(auto_now_add = True)
	initiate = models.BooleanField(default=False)
	complete = models.BooleanField(default=False)
	Task_highlight = models.CharField( max_length = 500,)
	author = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.taskname



class TaskComment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	task = models.ForeignKey(Task, related_name='taskcomment' ,  on_delete=models.CASCADE)
	comment_content = models.TextField( null= True , blank = True)
	published = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.author.username





class Event(models.Model):
	eventname = models.CharField(max_length = 500)
	event_descriptions = models.TextField() #remove null when go to deploy
	published = models.DateTimeField(auto_now_add = True)
	eventon = models.DateField()
	complete = models.BooleanField(default=False)
	event_highlight = models.CharField( max_length = 500,)
	author = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.author.username




class Wallet(models.Model):
	person_name = models.CharField(max_length = 500)
	published = models.DateTimeField(auto_now_add = True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.person_name


class Transistion(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	wallet = models.ForeignKey(Wallet, related_name='walletcomment' ,  on_delete=models.CASCADE  , null= True)
	comment = models.CharField(max_length = 500 , null=True)
	amount = models.IntegerField(null = True) 
	payment_status = models.CharField(max_length = 50 , choices  = Status ) #remove null when go to deploy
	payment_mode = models.CharField(max_length = 50 , choices  = Mode , null = True, blank=True)
	published = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.author.username

class Notes(models.Model):
	note = models.TextField() #remove null when go to deploy
	published = models.DateTimeField(auto_now_add = True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.author
